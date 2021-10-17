
import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from graphql_jwt.decorators import login_required

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


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True
        exclude_fields = ["related_category", ]

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (PlainTextNode, )
        filter_fields = ["id", ]
        filter_order_by = True
        exclude_fields = ["parent", ]

    # custome fields
    category_image = graphene.Field(ImageNode)

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        return queryset

    
    @classmethod
    @login_required
    def resolve_category_image(root, info, *args, **kwargs):
        return root.image



        