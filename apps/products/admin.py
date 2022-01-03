from django.contrib import admin
from django.apps import AppConfig
from .models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'discount',
        'description'
    ]


admin.site.register(Product, ProductsAdmin)
