import datetime

from django.db import models
from product.models import Product


class Sale(models.Model):
    sale_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "Sale " + str(self.id)

    def get_absolute_url(self):
        return f'/sale{self.id}'

    def amount_pm(self, all_amount=0):
        today = datetime.datetime.now()
        data = Sale.objects.filter(sale_date__year=today.year, sale_date__month=today.month, product=self.product)
        for i in data:
            all_amount += i.amount

        return all_amount

    def amount_of_proceeds(self):
        data = self.amount_pm() * self.product.price

        return data


    # def hide_date(self):
