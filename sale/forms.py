import datetime

from .models import Sale
from django.forms import ModelForm, DateInput, NumberInput


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_date', 'product', 'amount']

        widgets = {
            'sale_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': datetime.date.today(),
                'type': 'date'
            }),
            'product': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write product`s id'
            }),
            'amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write amount of products'
            })
        }


class SearchSaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_date']

        widgets = {
            'sale_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': datetime.date.today(),
                'type': 'date'
            })
        }