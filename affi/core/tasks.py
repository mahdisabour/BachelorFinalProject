from django.conf import settings

from ..celery import app
from .models import OTP

@app.task
def disableOTP(*args):
    instance = OTP.objects.get(id = args[0])
    instance.is_valid = False
    instance.save()