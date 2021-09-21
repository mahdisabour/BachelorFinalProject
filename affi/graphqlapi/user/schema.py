from affi.user.models import Role, User
from .types import UserInterface, UserNode, RoleNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField


class UserQuery(graphene.ObjectType):
    user = UserInterface.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    role = UserInterface.Field(RoleNode)
    all_roles = DjangoFilterConnectionField(RoleNode)
