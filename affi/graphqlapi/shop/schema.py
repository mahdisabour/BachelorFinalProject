import graphene
from graphene_django.filter import DjangoFilterConnectionField

from ...shop.models import Shop
from .types import PlainTextNode, ShopNode
from .filters import ShopFilter

class ShopQuery(graphene.ObjectType):
    shop = graphene.Field(ShopNode, id=graphene.Int())
    all_shop = DjangoFilterConnectionField(ShopNode, filterset_class=ShopFilter)

    def resolve_shop(self, info, id):
        return Shop.objects.filter(pk=id).first()
