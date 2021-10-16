import urllib.parse as urlparse
from urllib.parse import urlencode

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Affiliation


@receiver(post_save, sender=Affiliation)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        params = {
            "aff_id": instance.id
        }
        url = instance.related_product.related_shop.url
        instance.affiliation_url = create_url(url, params)
        instance.save()


def create_url(url, params):
    url_parse = urlparse.urlparse(url)
    query = url_parse.query
    url_dict = dict(urlparse.parse_qsl(query))
    url_dict.update(params)
    url_new_query = urlparse.urlencode(url_dict)
    url_parse = url_parse._replace(query=url_new_query)
    new_url = urlparse.urlunparse(url_parse)
    return new_url
