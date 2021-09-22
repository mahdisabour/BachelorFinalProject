from affi.user.models import User
from .types import UserInterface, UserNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField


class UserQuery(graphene.ObjectType):
    user = UserInterface.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
