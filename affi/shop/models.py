from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from ..core.models import User
from ..shop.tasks import woocommerece_handler
from . import ShopType
from .managers import ShopManager



class Shop(models.Model):

    objects = ShopManager()

    # name = models.CharField(max_length=50, blank=False)
    url = models.URLField(max_length=200, blank=False)
    type = models.CharField(max_length=50, choices=ShopType.CHOICES, default=ShopType.WOOCOMMERCE)
    shop_pic = models.ImageField(
        upload_to='profile/', default="profile/default_shop_pic.jpeg")
    is_staff = models.BooleanField(default=False)
    api_cunsumer_key = models.CharField(max_length=255, blank=True)
    api_secret_key = models.CharField(max_length=255, blank=True)
    data_ready = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.role = User.Roles.SHOP
            self.user.save()
        elif self.is_staff and not self.data_ready and self.api_cunsumer_key and self.api_secret_key:
            # woocommerece_handler.apply_async((self.pk, ))
            woocommerece_handler(self.pk)
        return super(Shop, self).save(*args, **kwargs)


class ShopRate(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    aff = models.ForeignKey("user.Aff", on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    rate = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    class Meta:
        unique_together = [
            ['aff', 'shop']
        ]