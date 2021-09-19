from django.db import models
from django.contrib.auth.models import User
from . import ShopType

# Create your models here.

class Shop(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField(max_length=200, blank=False)
    address = models.CharField(max_length=254, blank=True)
    type = models.CharField(max_length=50, choices=ShopType.CHOICES, default=ShopType.WOOCOMMERCE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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