from django.conf import settings

from woocommerce import API

from ..celery import app
from ..core.extract import CustomJsonExtraction
from ..product.models import Product


class WooCommerceHandler:
    def __init__(self, shop):
        # self.shop = Shop.objects.get(id=shop_id)
        self.shop = shop
        print(self.shop.api_cunsumer_key)
        self.wcapi = API(
            url=self.shop.url, # Your store URL
            consumer_key=self.shop.api_cunsumer_key, # Your consumer key
            consumer_secret=self.shop.api_secret_key, # Your consumer secret
            wp_api=True, # Enable the WP REST API integration
            version="wc/v3", # WooCommerce WP REST API version
            timeout=10
        )

    def get_products(self):
        print("get product started ...")
        products = self.wcapi.get("products").json()
        for product in products:
            extracted_data = self.extract_product_data(product)
            Product.objects.create(related_shop=self.shop, **extracted_data)
        print("products ready")

    def extract_product_data(self, json):
        print("extract data started ...")
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

    @app.task
    def run(self):
        self.get_products()
        print("task Done")
        self.shop.data_ready = True
        self.shop.save()
    
