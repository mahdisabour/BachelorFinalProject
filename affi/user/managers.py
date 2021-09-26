from django.contrib.auth.models import (
    BaseUserManager
)


class AffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results
        # return results.filter(type=User.Roles.SHOP)