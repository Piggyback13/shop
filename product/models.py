import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=50)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


