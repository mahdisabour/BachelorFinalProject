import graphene
from affi.core.models import User
from graphene import ObjectType, Field
import graphql_jwt

from .types import UserNode


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = Field(UserNode)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class CoreMutation(ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
