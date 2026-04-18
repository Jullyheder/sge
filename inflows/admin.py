from django.contrib import admin
from inflows.models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'supplier', 'product',
        'quantity', 'description', 'user_created',
        'user_updated', 'created_at', 'updated_at'
    ]
    search_fields = [
        'supplier__name', 'product__title',
        'user_created__username', 'user_updated__username'
    ]
