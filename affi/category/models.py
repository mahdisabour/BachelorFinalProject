from django.db import models
from mptt.models import MPTTModel
from mptt.managers import TreeManager

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, blank=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    display = models.CharField(max_length=50, blank=True)

    objects = models.Manager()
    tree = TreeManager()

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50, blank=True)
    related_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images") 
    src = models.ImageField(upload_to=None, blank=True)
    alt = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.related_category.name