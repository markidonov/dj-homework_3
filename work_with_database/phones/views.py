from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_type = request.GET.get('sort')
    if sort_type == 'name':
        phones = phones.order_by('name')
    if sort_type == 'min_price':
        phones = phones.order_by('price')
    if sort_type == 'max_price':
        phones = phones.order_by('-price')
    template = 'catalog.html'
    context = {'phones': phones,}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
