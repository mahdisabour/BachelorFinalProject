
import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from graphql_jwt.decorators import login_required

from affi.graphqlapi.product.filters import ProductFilter


from ...product.models import (
    ProductImage,
    Dimension,
    Download,
    Tag,
    Review,
    Product
)
from ..category.types import CategoryNode


class PlainTextNode(relay.Node):
    class Meta:
        name = 'productNetwork'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class ProductImageNode(DjangoObjectType):
    class Meta:
        model = ProductImage
        interfaces = (PlainTextNode, )
        filter_fields = ["name", ]
        # filter_order_by = True



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
        filterset_class = ProductFilter
        filter_order_by = True
        # exclude_fields = ["images", ]

    # custom fields
    images = graphene.List(ProductImageNode)
    dimensions = graphene.List(DimensionNode)
    downloads = graphene.List(DownloadNode)
    tags = graphene.List(TagNode)
    categories = graphene.List(CategoryNode)

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        return queryset

    @staticmethod
    @login_required
    def resolve_images(root, info, **kwargs):
        return root.images.all()

    @staticmethod
    @login_required
    def resolve_dimensions(root, info, **kwargs):
        return root.dimensions.all()

    @staticmethod
    @login_required
    def resolve_downloads(root, info, **kwargs):
        return root.downloads.all()

    @staticmethod
    @login_required
    def resolve_tags(root, info, **kwargs):
        return root.tags.all()

    @staticmethod
    @login_required
    def resolve_categories(root, *args, **kwargs):
        return root.categories.all()
