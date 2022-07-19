import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .forms import SaleForm, SearchSaleForm
from django.views.generic import DetailView, UpdateView

from .models import Sale


def sale(request):
    if request.method == 'POST':
        form = SearchSaleForm(request.POST)
        if form.is_valid():
            hide_data = form.data['sale_date']
            sales = Sale.objects.all().exclude(sale_date=hide_data)
            return render(request, 'sales.html', {'sales': sales, 'form': form})
        else:
            error = 'Sorry, form filled out incorrectly'
    elif request.method == 'GET':
        form = SearchSaleForm()
        sales = Sale.objects.all().order_by('-sale_date')
    return render(request, 'sales.html', {'sales': sales, 'form': form})


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'details_view.html'
    context_object_name = 'sale'


class SaleUpdateView(UpdateView):
    model = Sale
    template_name = 'create.html'
    form_class = SaleForm


def create(request):
    error = ''
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        if sale_form.is_valid():
            sale_form.save()
            return redirect('sale')
        else:
            error = 'Sorry, form filled out incorrectly'

    sale_form = SaleForm()

    data = {
        'sale_form': sale_form,
        'error': error
    }

    return render(request, 'create.html', data)


def update(request, pk):
    error = ''
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale_form = SaleForm(request.POST, instance=sale)
        if sale_form.is_valid():
            sale_form.save()
            return redirect('sale')
        else:
            error = 'Sorry, form filled out incorrectly'

    sale_form = SaleForm(instance=sale)

    data = {
        'sale_form': sale_form,
        'error': error
    }

    return render(request, 'create.html', data)


def amount_pm(request):
    today = datetime.datetime.now()
    data = Sale.objects.filter(sale_date__year=today.year, sale_date__month=today.month)

    return render(request, data)
