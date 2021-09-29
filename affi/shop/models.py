from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from ..core.models import User
from . import ShopType
from .managers import ShopManager



class Shop(models.Model):

    objects = ShopManager()

    name = models.CharField(max_length=50, blank=False)
    url = models.URLField(max_length=200, blank=False)
    type = models.CharField(max_length=50, choices=ShopType.CHOICES, default=ShopType.WOOCOMMERCE)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.role = User.Roles.SHOP
            self.user.save()
        return super().save(*args, **kwargs)


class ShopImage(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    related_shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="images")
    name = models.CharField(max_length=50, blank=True)
    src = models.ImageField(upload_to="shop/", blank=True)
    alt = models.CharField(max_length=50, blank=True)
    def __str__(self) -> str:
        return self.name