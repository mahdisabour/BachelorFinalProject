import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene import ObjectType

from ...category.models import Category

from .types import (
    CategoryNode,
    ImageNode,
    PlainTextNode
)


class CategoryQuery(ObjectType):
    all_category = DjangoFilterConnectionField(CategoryNode)
    parent_categories = graphene.List(CategoryNode)
    child_categories_by_parent_base_id = graphene.List(
        CategoryNode, parent_base_id=graphene.Int())

    def resolve_parent_categories(self, info):
        return Category.objects.filter(parent=0)

    def resolve_child_categories_by_base_id(self, info, parent_base_id):
        return Category.objects.filter(parent=parent_base_id)