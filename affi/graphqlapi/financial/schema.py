from affi.graphqlapi.shop.types import PlainTextNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .types import WalletNode, PlainTextNode


class FinancialQuery(graphene.ObjectType):
    wallet = PlainTextNode.Field(WalletNode)
    all_wallet = DjangoFilterConnectionField(WalletNode)
