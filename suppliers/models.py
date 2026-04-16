from django.db import models
from accounts.models import User


class Supplier(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    user_created = models.ForeignKey(
        User,
        related_name='supplier_created_by',
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    user_updated = models.ForeignKey(
        User,
        related_name='supplier_updated_by',
        on_delete=models.PROTECT,
        null=True, blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name
