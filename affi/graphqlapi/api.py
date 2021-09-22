import graphene

from .user.schema import UserQuery
from .shop.schema import ShopQuery
from .category.schema import CategoryQuery
from .product.schema import ProductQuery


class Query(
    ShopQuery,
    UserQuery,
    CategoryQuery,
    ProductQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
