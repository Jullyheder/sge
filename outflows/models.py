from django.db import models
from accounts.models import User
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(
        Product, related_name='outflows', on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    user_created = models.ForeignKey(
        User, related_name='created_outflows_by', on_delete=models.PROTECT
    )
    user_updated = models.ForeignKey(
        User, related_name='updated_outflows_by', on_delete=models.PROTECT, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Outflow'
        verbose_name_plural = 'Outflows'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
