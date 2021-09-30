from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from mptt.models import MPTTModel
from mptt.managers import TreeManager

from ..core.models import ModelWithMetaData

from ..category.models import Category

from . import CatalogVisibilityType, ProductType, ReviewStatus, ProductStatus, StockStatus, TaxStatus
# Create your models here.


class Image(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    related_product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="images")
    name = models.CharField(max_length=50, blank=True)
    src = models.ImageField(upload_to=None, blank=True)
    alt = models.CharField(max_length=50, blank=True)


class Dimension(models.Model):
    length = models.IntegerField(blank=True)
    width = models.IntegerField(blank=True)
    heigth = models.IntegerField(blank=True)
    related_product = models.OneToOneField(
        "product.Product", on_delete=models.CASCADE, related_name="dimensions")


class Download(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="downloads/", max_length=100)
    related_product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="downloads")


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True)


class Review(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    related_product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="reviews")
    status = models.CharField(
        max_length=50, choices=ReviewStatus.CHOICES, default=ReviewStatus.APPROVED)  # choices
    reviewer = models.CharField(max_length=50)
    reviewer_email = models.EmailField(max_length=254)
    review = models.TextField(max_length=254, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True)
    verified = models.BooleanField(default=False)


class Product(ModelWithMetaData):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=255, unique=True,
                            allow_unicode=True, blank=True)
    permalink = models.URLField(max_length=200, blank=True)
    type = models.CharField(
        max_length=50, choices=ProductType.CHOICES, default=ProductType.SIMPLE)  # choices
    status = models.CharField(
        max_length=50, blank=True, choices=ProductStatus.CHOICES, default=ProductStatus.PUBLISH)  # choices
    featured = models.BooleanField(default=False)
    catalog_visibility = models.CharField(
        max_length=50, choices=CatalogVisibilityType.CHOICES, default=CatalogVisibilityType.VISIBLE)  # choices
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=254, blank=True)
    sku = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=50, blank=True)
    regular_price = models.CharField(max_length=50, blank=True)
    sale_price = models.CharField(max_length=50, blank=True)
    date_on_sale_from = models.DateTimeField(blank=True, null=True)
    date_on_sale_to = models.DateTimeField(blank=True, null=True)
    price_html = models.CharField(max_length=50, blank=True)
    on_sale = models.BooleanField(blank=True)
    purchasable = models.BooleanField(blank=True)
    total_sales = models.IntegerField(blank=True, null=True)
    virtual = models.BooleanField(default=False, blank=True)
    downloadable = models.BooleanField(default=False, blank=True)
    download_limit = models.IntegerField(default=-1, blank=True, null=True)
    download_expiry = models.IntegerField(default=-1, blank=True, null=True)
    external_url = models.URLField(max_length=200, blank=True)
    button_text = models.CharField(max_length=50, blank=True)
    tax_status = models.CharField(
        max_length=50, choices=TaxStatus.CHOICES, default=TaxStatus.TAXABLE)  # choices
    manage_stock = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(blank=True, null=True)
    stock_status = models.CharField(
        max_length=50, choices=StockStatus.CHOICES, default=StockStatus.INSTOCK)  # choices
    backordered = models.BooleanField(blank=True)
    sold_individually = models.BooleanField(default=False)
    weight = models.CharField(max_length=50, blank=True)
    shipping_required = models.BooleanField(blank=True)
    shipping_taxable = models.BooleanField(blank=True)
    reviews_allowed = models.BooleanField(default=True)
    average_rating = models.CharField(max_length=50, default=0)
    rating_count = models.IntegerField(blank=True, null=True)
    related_ids = models.ManyToManyField("self", blank=True)
    cross_sell_ids = models.ManyToManyField("self", blank=True)
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True)
    purchase_note = models.CharField(max_length=50, blank=True)
    categories = models.ManyToManyField("category.Category", blank=True)
    tags = models.ManyToManyField("product.Tag", blank=True)
    menu_order = models.IntegerField(blank=True, null=True)
    affiliate_rate = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    related_shop = models.ForeignKey(
        "shop.Shop", on_delete=models.CASCADE, null=True, related_name="products")
