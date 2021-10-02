from django.db.models.signals import post_save
from django.dispatch import receiver

from ..financial.models import Wallet
from .models import User


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(
            user=instance
        )  