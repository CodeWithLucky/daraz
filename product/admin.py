from django.contrib import admin
from . models import Category, Product, Color, Size

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'stock_quantity', 'category', 'description',
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'image', 'created_at'
    ]
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)