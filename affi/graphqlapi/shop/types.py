import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from graphql_jwt.decorators import login_required

from ...shop.models import Shop, ShopImage


class PlainTextNode(relay.Node):
    class Meta:
        name = 'shopNetwork'

    @staticmethod
    def to_global_id(type, id):
        print(id, "to global id")
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class ShopImageNode(DjangoObjectType):
    class Meta:
        model = ShopImage
        interfaces = (PlainTextNode, )
        filter_fields = ['id', ]
        filter_order_by = True
        exclude_fields = ["related_shop", ]

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        interfaces = (PlainTextNode, )
        filter_fields = {
            'id':['exact'],
        } 
        filter_order_by = True
        exclude_fields = ["images", ]

    # custome Field
    shop_image = graphene.List(ShopImageNode)
    products_count = graphene.Int()

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)

    
    @staticmethod
    @login_required
    def resolve_shop_image(root, info, **kwargs):
        return root.images.all()

    
    @staticmethod
    @login_required
    def resolve_products_count(root, info, **kwargs):
        return root.products.all().count()