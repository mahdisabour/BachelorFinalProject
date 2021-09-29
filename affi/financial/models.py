from django.db import models



class Wallet(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.BigIntegerField(default=0)
    bank_account_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(
        max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField("core.User", on_delete=models.CASCADE)


# class Transaction(models.Model):
#     pass