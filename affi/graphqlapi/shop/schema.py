import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .types import PlainTextNode, ShopImageNode, ShopNode


class ShopQuery(graphene.ObjectType):
    # shop = PlainTextNode.Field(ShopNode)
    all_shop = DjangoFilterConnectionField(ShopNode)

    # shop_image = PlainTextNode.Field(ShopImageNode)
    all_shop_image = DjangoFilterConnectionField(ShopImageNode)
    
