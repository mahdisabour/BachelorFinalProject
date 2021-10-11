from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from ..core.models import User


class Aff(models.Model):
    age = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(null=True)
    national_code = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.role = User.Roles.AFF
            self.user.save()
        return super().save(*args, **kwargs)


