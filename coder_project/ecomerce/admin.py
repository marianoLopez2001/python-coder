from django.contrib import admin
from ecomerce.models import Productos, Carritos, Cliente
# Register your models here.

@admin.register(Productos)
class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'id')
    list_filter = ['price']
    search_fields = ["name"]

@admin.register(Carritos)
class CartAdmin (admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ["name"]

@admin.register(Cliente)
class ClientAdmin (admin.ModelAdmin):
    list_display = ('name', 'lastName', 'id')
    list_filter = ["lastName"]
    search_fields = ["name"]