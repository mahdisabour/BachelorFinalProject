from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product, Image


@receiver(post_save, sender=Product)
def create_default_image(sender, instance, created, **kwargs):
    if created:
        Image.objects.create(
            related_product=instance, 
            name="default_product_pic", 
            alt="default_product_pic"
        )