from django.contrib import admin
from catalog.models import Product, Category, Record

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'description')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'unit_price', 'category_id')
    search_fields = ('product_name', 'description')
    list_filter = ('category_id',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}


