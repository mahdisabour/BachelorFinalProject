from .types import PlainTextNode, ShopNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField


class ShopQuery(graphene.ObjectType):
    shop = PlainTextNode.Field(ShopNode)
    all_shop = DjangoFilterConnectionField(ShopNode)


