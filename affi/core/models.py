from django.db import models

# Create your models here.


class ModelWithMetaData(models.Model):
    metadata = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        abstract = True

    def clear_metadata(self):
        self.metadata = {}
    