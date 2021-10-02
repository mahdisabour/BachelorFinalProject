import graphene
from graphene_django import DjangoObjectType
from graphene import relay, InputObjectType
from graphql_jwt.decorators import login_required

from ...core.models import User


class UserInterface(relay.Node):
    class Meta:
        name = 'coreNode'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def from_global_id(global_id):
        return global_id.split(':')


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (UserInterface, )
        filter_fields = {
            'id': ['exact'],
            'phone_number': ['exact']
        }
        filter_order_by = True

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        super().get_queryset(queryset, info)


class CreateUserInputType(InputObjectType):
    phone_number = graphene.String(required=True)
    password = graphene.String(required=True)
    email_address = graphene.String(required=True)


class UserUpdateInputType(InputObjectType):
    address = graphene.String()

