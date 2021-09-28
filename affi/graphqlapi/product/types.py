
from graphene_django import DjangoObjectType
from graphene import relay
from graphql_jwt.decorators import login_required



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

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class DimensionNode(DjangoObjectType):
    class Meta:
        model = Dimension
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class DownloadNode(DjangoObjectType):
    class Meta:
        model = Download
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


