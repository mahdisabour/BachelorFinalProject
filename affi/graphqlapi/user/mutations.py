import graphene
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required

from ..core.types import CreateUserInputType
from ...core.models import User
from ...user.models import Aff
from ..core.types import UserUpdateInputType
from .types import AffUpdateInputType


class CreateAff(graphene.Mutation):
    class Arguments:
        user_data = CreateUserInputType(required=True)
        national_code = graphene.String(required=True)
        full_name = graphene.String(required=True)

    status = graphene.String()

    @login_required
    def mutate(self, info, user_data, **kwargs):
        user = User(
            phone_number=user_data.get("phone_number"),
            email=user_data.get("email_address")
        )
        user.set_password(user_data.get("password"))
        user.save()

        Aff.objects.create(
            user=user,
            full_name=kwargs.get("full_name"),
            national_code=kwargs.get("national_code"),
        )
        return CreateAff(status="Success")


class UpdateAff(graphene.Mutation):
    class Arguments:
        aff_data = AffUpdateInputType()
        user_data = UserUpdateInputType()

    status = graphene.String()

    @login_required
    def mutate(self, info, aff_data, user_data):
        user = info.context.user
        # update user values
        if user_data:
            for key, val in user_data.items():
                if val:
                    setattr(user, key, val)
            user.save()
        try:
            shop = Aff.objects.get(user__phone_number=user.phone_number)
        except:
            return UpdateAff(status="fail, you are not shop")
        # update shop values
        if aff_data:
            for key, val in aff_data.items():
                if val:
                    setattr(shop, key, val)
            shop.save()

        return UpdateAff(status="success")


class UserMutation(graphene.ObjectType):
    create_aff = CreateAff.Field()
    update_aff = UpdateAff.Field()