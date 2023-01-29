from django.contrib import admin
from ecommerce.models import Productos, Community
# Register your models here.

@admin.register(Productos)
class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'id')
    list_filter = ['price']
    search_fields = ["name"]

@admin.register(Community)
class CommunityAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'id')
    list_filter = ['id']
    search_fields = ["name"]