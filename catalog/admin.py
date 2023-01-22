from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'unit_price', 'category_name')
    search_fields = ('product_name', 'description')
    list_filter = ('category_name',)