from django.db import models


class Account(models.Model):
    detail = models.CharField(max_length=255)
    debit = models.CharField(max_length=20)
    credit = models.CharField(max_length=20)
