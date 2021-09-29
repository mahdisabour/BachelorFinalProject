from graphene_django import DjangoObjectType
from graphene import relay
from graphql_jwt.decorators import login_required

from ...financial.models import Wallet


class PlainTextNode(relay.Node):
    class Meta:
        name = 'financialNode'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class WalletNode(DjangoObjectType):
    class Meta:
        model = Wallet
        interfaces = (PlainTextNode, )
        filter_fields = {}

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)