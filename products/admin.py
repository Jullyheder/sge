from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'brand', 'category',
        'user_created', 'user_updated',
        'created_at', 'updated_at'
    ]
    search_fields = [
        'title', 'brand__name', 'category__name',
        'user_created__username', 'user_updated__username'
    ]
