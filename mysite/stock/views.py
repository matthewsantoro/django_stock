from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic import View
from .models import Product
# Create your views here.


class ProductInStock(View):
    def get(self, request):
        products = Product.objects.filter(status=1)
        return render(request, 'stock/products.html', context={'products': products})


class ProductDiscarded(View):
    def get(self, request):
        products = Product.objects.filter(status=2)
        return render(request, 'stock/products_discarded.html', context={'products': products})


class ProductdDelivered(View):
    def get(self, request):
        products = Product.objects.filter(status=3)
        return render(request, 'stock/products_delivered.html', context={'products': products})


class ProductDetail(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'stock/product_detail.html', context={'product': product})


class ModalProductDetail(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'stock/modal_product_detail', context={'product': product})
        
