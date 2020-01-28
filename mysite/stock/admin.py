from django.contrib import admin
from .models import Products, Ranks, Statuses

admin.site.register(Products)
admin.site.register(Ranks)
admin.site.register(Statuses)