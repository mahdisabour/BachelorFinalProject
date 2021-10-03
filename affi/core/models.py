from random import randint

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


def random_with_N_digits():
    n = settings.OTP_NUMBER_OF_DIGITS
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return str(randint(range_start, range_end))


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

    username = None
    first_name = None
    last_name = None
    is_staff = None
    # add additional fields in here
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.ADMIN)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class OTP(models.Model):
    message = models.CharField(
        max_length=7, default=random_with_N_digits, blank=True, null=True)
    is_valid = models.BooleanField(default=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="OTP")

    def __str__(self):
        return f"{self.profile.user.username}"