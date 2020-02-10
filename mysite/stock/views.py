from django.shortcuts import render
from django.views.generic import View
from .models import  Products
# Create your views here.

class ProductInStock(View):
    def get(self,request):
        products = Products.objects.all()
        return render(request, 'stock/in_stock.html', context={'products': products})