import graphene
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required


from ..core.types import CreateUserInputType
from ...core.models import User
from ...shop.models import Shop, ShopRate
from ...user.models import Aff
from ..core.types import UserUpdateInputType
from .types import ShopUpdateInputType


class CreateShop(graphene.Mutation):
    class Arguments:
        user_data = CreateUserInputType(required=True)
        name = graphene.String(required=True)
        url = graphene.String(required=True)

    status = graphene.String()

    @login_required
    def mutate(self, info, user_data, **kwargs):
        user = User(
            phone_number=user_data.get("phone_number"),
            email=user_data.get("email_address")
        )
        user.set_password(user_data.get("password"))
        user.save()

        Shop.objects.create(
            user=user, 
            name=kwargs.get("name"),
            url=kwargs.get("url")
        )
        return CreateShop(status="success")


class UpdateShop(graphene.Mutation):
    class Arguments:
        shop_data = ShopUpdateInputType()
        user_data = UserUpdateInputType()

    status = graphene.String()

    @login_required
    def mutate(self, info, shop_data, user_data):
        user = info.context.user
        # update user values
        if user_data:
            for key, val in user_data.items():
                if val:
                    setattr(user, key, val)
            user.save()
        try:
            shop = Shop.objects.get(user__phone_number=user.phone_number)
        except:
            return UpdateShop(status="fail, you are not shop")
        # update shop values
        if shop_data:
            for key, val in shop_data.items():
                if val:
                    setattr(shop, key, val)
            shop.save()

        return UpdateShop(status="success")


class RateShop(graphene.Mutation):
    class Arguments:
        rate = graphene.Int(required=True)
        shop_id = graphene.Int(required=True)

    status = graphene.String()

    @login_required
    def mutate(self, info, rate, shop_id):
        if Aff.objects.filter(user__phone_number=info.context.user.phone_number).exists():
            aff = Aff.objects.filter(user__phone_number=info.context.user.phone_number).first()
        else: 
            return RateShop("you are not aff user")
        shop = Shop.objects.get(id=shop_id)
        if ShopRate.objects.filter(aff=aff, shop=shop).exists():
            shop_rate = ShopRate.objects.get(aff=aff, shop=shop)
            shop_rate.rate = rate
            shop_rate.save()
        else:
            ShopRate.objects.create(
                aff= aff,
                shop=shop,
                rate=rate
            )
        return RateShop(status="success")


class ShopMutation(graphene.ObjectType):
    create_shop = CreateShop.Field()
    rate_shop = RateShop.Field()
    update_shop = UpdateShop.Field()
