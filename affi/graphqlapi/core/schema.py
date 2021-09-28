from .types import UserInterface, UserNode
import graphene
from graphene_django.filter import DjangoFilterConnectionField

from ...core.models import User


class CoreQuery(graphene.ObjectType):
    user = graphene.Field(UserNode, id=graphene.Int())
    all_users = DjangoFilterConnectionField(UserNode)


    def resolve_user(self, info, id):
        return User.objects.filter(pk=id).first()

