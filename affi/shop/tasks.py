from django.conf import settings

from woocommerce import API

from ..celery import app
from ..core.extract import CustomJsonExtraction
from ..product.models import Product
from ..product.models import ProductImage
from ..category.models import Category, Image
from ..shop import models as ShopModels


class WooCommerceHandler:
    def __init__(self, shop):
        # self.shop = Shop.objects.get(id=shop_id)
        self.shop = shop
        self.wcapi = API(
            url=self.shop.url,  # Your store URL
            consumer_key=self.shop.api_cunsumer_key,  # Your consumer key
            consumer_secret=self.shop.api_secret_key,  # Your consumer secret
            wp_api=True,  # Enable the WP REST API integration
            version="wc/v3",  # WooCommerce WP REST API version
            timeout=10
        )

    def get_products(self):
        products = self.wcapi.get("products", params={'per_page': 100}).json()
        for product in products:
            extracted_data = self.extract_product_data(product)
            product_obj = Product.objects.create(
                related_shop=self.shop, base_id=product["id"], **extracted_data)
            if product["images"]:
                for image in product["images"]:
                    image_extracted_data = self.extract_image_data(
                        image
                    )  # extract product image data
                    ProductImage.objects.create(
                        related_product=product_obj, base_id=image["id"], **image_extracted_data)
            # save product category
            if product["categories"]:
                for category in product["categories"]:
                    cat_obj = Category.objects.get(base_id=category["id"])
                    product_obj.categories.add(cat_obj)



    def extract_product_data(self, json):
        exclude_fields = [
            "id",
            "related_ids",
            "cross_sell_ids",
            "categories",
            "tags",
            "related_shop",
            "downloads",
            "dimensions",
            "images",
        ]
        product_json_extraction = CustomJsonExtraction(
            model=Product,
            exclude_fields=exclude_fields
        )
        data = product_json_extraction.extract_data(json)
        return data

    def get_categories(self):
        categories = self.wcapi.get(
            "products/categories", params={'per_page': 100, 'order': 'asc', "orderby": "id"}).json()
        for cat in categories:  # handle data for each category
            extracted_data = self.extract_category_data(
                cat
            )  # extract category data
            category = Category.objects.create(
                related_shop=self.shop, base_id=cat["id"], **extracted_data
            )
            if cat["image"]:
                image_extracted_data = self.extract_image_data(
                    cat["image"]
                )  # extract category image data
                Image.objects.create(
                    related_category=category, base_id=cat["image"]["id"], **image_extracted_data)

    def extract_category_data(self, json):
        exclude_fields = [
            "id",
            "image",
        ]
        category_json_extraction = CustomJsonExtraction(
            model=Category,
            exclude_fields=exclude_fields
        )
        data = category_json_extraction.extract_data(json)
        return data

    def extract_image_data(self, json):
        exclude_fields = [
            "id"
        ]
        category_image_extraction = CustomJsonExtraction(
            model=Image,
            exclude_fields=exclude_fields
        )
        data = category_image_extraction.extract_data(json)
        return data

    def run(self):
        self.get_categories()
        self.get_products()
        self.shop.data_ready = True
        self.shop.save()



@app.task
def woocommerece_handler(*args):
    shop = ShopModels.Shop.objects.get(id=args[0])
    print(shop.url)
    woocommerce_handler = WooCommerceHandler(shop=shop)
    woocommerce_handler.run()
