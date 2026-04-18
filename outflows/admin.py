from django.contrib import admin
from outflows.models import Outflow


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = [
        'product', 'quantity', 'description',
        'user_created', 'user_updated', 'created_at',
        'updated_at'
    ]
    search_fields = [
        'product__title', 'user_created__username', 'user_updated__username'
    ]
