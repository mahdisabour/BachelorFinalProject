from graphene_django import DjangoObjectType
from graphene import relay
from graphql_jwt.decorators import login_required

from ...core.models import User


class UserInterface(relay.Node):
    class Meta:
        name = 'coreNode'

    @staticmethod
    def to_global_id(type, id):
        print("to global id")
        return id

    @staticmethod
    def from_global_id(global_id):
        print("from global id")
        print(global_id)
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

