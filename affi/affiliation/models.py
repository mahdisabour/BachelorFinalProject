from django.db import models

from . import OrderStatus


class Affiliation(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    affiliator = models.ForeignKey("user.Aff", on_delete=models.CASCADE)
    related_product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE)
    affiliation_url = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = [
            ['affiliator', 'related_product']
        ]

    def __str__(self) -> str:
        return f"{self.affiliator.user.name}, {self.related_product.name}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    base_order_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=OrderStatus.CHOICES, default=OrderStatus.SUCCESS)
    related_affiliation = models.ForeignKey(
        Affiliation, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.related_affiliation.related_product.name}, {self.related_affiliation.related_product.related_shop.user.name}"
