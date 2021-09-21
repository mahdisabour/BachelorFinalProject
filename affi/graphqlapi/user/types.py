from graphene_django import DjangoObjectType
from graphene import relay

from affi.user.models import User, Role


class UserInterface(relay.Node):
    class Meta:
        name = 'user'

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
        filter_fields = ['id', ]
        filter_order_by = True


class RoleNode(DjangoObjectType):
    class Meta:
        model = Role
        interfaces = (UserInterface, )
        filter_fields = ['id', ]
        filter_order_by = True
