from django.shortcuts import render
from django.views.generic import View
from .models import Products
# Create your views here.


class ProductInStock(View):
    def get(self, request):
        products = Products.objects.filter(status=1)
        table_name = 'На складе'
        return render(request, 'stock/products.html', context={'products': products, 'table_name': table_name})


class ProductDiscarded(View):
    def get(self, request):
        table_name = 'Списан'
        products = Products.objects.filter(status=2)
        return render(request, 'stock/products.html', context={'products': products})


class ProductdDelivered(View):
    def get(self, request):
        table_name = 'Выдан'
        products = Products.objects.filter(status=3)
        return render(request, 'stock/products.html', context={'products': products})
