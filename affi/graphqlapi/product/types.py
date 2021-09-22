
from graphene_django import DjangoObjectType
from graphene import relay

from ...product.models import (
    Image, 
    Dimension, 
    Download, 
    Tag, 
    Review, 
    Product
)


class PlainTextNode(relay.Node):
    class Meta:
        name = 'productNetwork'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


class DimensionNode(DjangoObjectType):
    class Meta:
        model = Dimension
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


class DownloadNode(DjangoObjectType):
    class Meta:
        model = Download
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True


