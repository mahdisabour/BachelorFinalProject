from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager



class ModelWithMetaData(models.Model):
    metadata = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        abstract = True

    def clear_metadata(self):
        self.metadata = {}


class User(AbstractUser):
    objects = CustomUserManager()

    class Roles(models.TextChoices):
        AFF = "AFF", "Aff"
        SHOP = "SHOP", "Shop"
        ADMIN = "ADMIN", "Admin"

    # add additional fields in here
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    bank_account_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(
        max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.ADMIN)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
