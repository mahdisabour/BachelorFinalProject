from django.contrib.auth.models import BaseUserManager

from ..user.models import User


class ShopManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Roles.SHOP)