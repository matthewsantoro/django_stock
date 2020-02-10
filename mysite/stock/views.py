from django.shortcuts import render
from django.views.generic import View
from .models import  Products
# Create your views here.

class ProductList(View):
    def get(self,request):
        product = Products.objects.all()
        return render(request, 'stock/index.html', context={'product': product})