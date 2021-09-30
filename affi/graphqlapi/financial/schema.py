from affi.graphqlapi.shop.types import PlainTextNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .types import WalletNode, PlainTextNode, TransactionNode
from ...financial.models import Wallet

class FinancialQuery(graphene.ObjectType):
    wallet = graphene.Field(WalletNode, user_id=graphene.Int())
    # all_wallet = DjangoFilterConnectionField(WalletNode)

    transaction = PlainTextNode.Field(TransactionNode)

    def resolve_wallet(self, info, user_id):
        return Wallet.objects.filter(user__pk=user_id).first()
