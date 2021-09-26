from graphene_django import DjangoObjectType
from graphene import relay

from ...user.models import Aff


class PlainTextNode(relay.Node):
    class Meta:
        name = 'userNode'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class AffNode(DjangoObjectType):
    class Meta:
        model = Aff
        interfaces = (PlainTextNode, )
        filter_fields = ['id', ]
        filter_order_by = True
