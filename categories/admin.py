from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user_created', 'user_updated', 'created_at', 'updated_at']
    search_fields = ['name', 'user_created__username', 'user_updated__username']
