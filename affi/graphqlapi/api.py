import graphene
from .shop.schema import ShopQuery


class Query(
    ShopQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    graphene.ObjectType
):
    pass



schema = graphene.Schema(query=Query)
