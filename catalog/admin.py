from django.contrib import admin
from catalog.models import Product, Category, Version

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'version_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('is_active',)