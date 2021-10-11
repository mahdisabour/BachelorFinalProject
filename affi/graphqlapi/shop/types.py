from django.db.models import Avg

import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required

from ...shop.models import Shop, ShopRate


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


class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        interfaces = (PlainTextNode, )
        filter_fields = {
            'id':['exact'],
        } 
        filter_order_by = True
        exclude_fields = []

    # custome Field
    products_count = graphene.Int()
    shop_rate = graphene.Float()

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)

    
    @staticmethod
    @login_required
    def resolve_products_count(root, info, **kwargs):
        return root.products.all().count()

    
    @staticmethod
    @login_required
    def resolve_shop_rate(root, info, **kwargs):
        rate = ShopRate.objects.filter(shop=root).aggregate(Avg("rate"))
        return rate["rate__avg"]


class ShopUpdateInputType(graphene.InputObjectType):
    url = graphene.String()
    shop_pic = Upload()
