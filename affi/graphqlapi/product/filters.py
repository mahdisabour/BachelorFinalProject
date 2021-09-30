from django.db.models import fields
import django_filters

from ...product.models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="categories__name", lookup_expr="exact")
    order_by = django_filters.OrderingFilter(
        fields=(
            '-affiliate_rate',
            'affiliate_rate',
            'name',
        )
    )

    class Meta:
        model = Product
        fields = []
