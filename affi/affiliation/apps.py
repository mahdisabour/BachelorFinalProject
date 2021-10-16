from django.apps import AppConfig


class AffiliationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'affi.affiliation'

    def ready(self) -> None:
        from . import signals
        return super().ready()
