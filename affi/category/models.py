from django.db import models
from mptt.models import MPTTModel
from mptt.managers import TreeManager

# Create your models here.


class Category(models.Model):
    base_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True,
                            allow_unicode=True, blank=True)
    description = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    display = models.CharField(max_length=50, blank=True)
    related_shop = models.ForeignKey(
        "shop.Shop", on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()
    tree = TreeManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = [
            ['id', 'related_shop']
        ]


class Image(models.Model):
    base_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    related_category = models.OneToOneField(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="image")
    src = models.URLField(max_length=200, blank=True, null=True)
    alt = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.related_category.name
