from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'affi.product'

    def ready(self) -> None:
        from . import signals
        return super().ready()
