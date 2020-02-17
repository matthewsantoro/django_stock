from django.contrib import admin
from .models import Product, Rank, Status

admin.site.register(Product)
admin.site.register(Rank)
admin.site.register(Status)