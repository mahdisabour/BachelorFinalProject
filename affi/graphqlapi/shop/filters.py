import django_filters

from ...shop.models import Shop

class ShopFilter(django_filters.FilterSet):
    user = django_filters.BaseInFilter(field_name="user__pk", lookup_expr="in")

    class Meta:
        model = Shop
        fields = ['user', ]