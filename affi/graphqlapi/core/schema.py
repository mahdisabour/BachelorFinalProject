from .types import UserInterface, UserNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField


class CoreQuery(graphene.ObjectType):
    user = UserInterface.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
