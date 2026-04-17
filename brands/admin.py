from django.contrib import admin
from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user_created', 'user_updated', 'created_at', 'updated_at']
    search_fields = ['name', 'user_created__username', 'user_updated__username']
