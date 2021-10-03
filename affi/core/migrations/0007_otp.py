# Generated by Django 3.2.7 on 2021-10-03 07:58

import affi.core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211002_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, default=affi.core.models.random_with_N_digits, max_length=7, null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OTP', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]