from graphene import ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .types import (
    PlainTextNode, 
    AffNode
)


class UserQuery(ObjectType):
    Aff = PlainTextNode.Field(AffNode)
    all_aff = DjangoFilterConnectionField(AffNode)