
from graphene_django import DjangoObjectType
from graphene import relay

from ...category.models import Category, Image


class PlainTextNode(relay.Node):
    class Meta:
        name = 'categoryNetwork'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True

        