from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

exlude_model_name = []

app_models = apps.get_app_config('affiliation').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass