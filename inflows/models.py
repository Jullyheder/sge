from django.db import models
from accounts.models import User
from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(
        Supplier, related_name='inflows', on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name='inflows', on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    user_created = models.ForeignKey(
        User, related_name='created_inflows_by', on_delete=models.PROTECT
    )
    user_updated = models.ForeignKey(
        User, related_name='updated_inflows_by', on_delete=models.PROTECT, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inflow'
        verbose_name_plural = 'Inflows'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
