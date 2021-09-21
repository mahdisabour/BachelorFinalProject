from .user.schema import UserQuery
import graphene
from .shop.schema import ShopQuery


class Query(
    ShopQuery,
    UserQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
