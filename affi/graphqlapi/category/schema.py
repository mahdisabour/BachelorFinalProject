from graphene_django.filter import DjangoFilterConnectionField
from graphene import ObjectType

from .types import (
    CategoryNode, 
    ImageNode, 
    PlainTextNode
)


class CategoryQuery(ObjectType):
    # category = PlainTextNode.Field(CategoryNode)
    all_category = DjangoFilterConnectionField(CategoryNode)

    # category_image = PlainTextNode.Field(ImageNode)
    all_category_image = DjangoFilterConnectionField(ImageNode)