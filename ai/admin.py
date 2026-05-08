from django.contrib import admin
from ai import models


@admin.register(models.AIResult)
class AIResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'created_at')
    readonly_fields = ('result', 'created_at')
