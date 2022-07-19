from django.shortcuts import render
from .models import Product


def product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


