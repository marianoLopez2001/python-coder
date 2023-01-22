from django.contrib import admin
from ecommerce.models import Productos
# Register your models here.

@admin.register(Productos)
class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'id')
    list_filter = ['price']
    search_fields = ["name"]
