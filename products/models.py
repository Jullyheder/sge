from django.db import models
from accounts.models import User
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=500)
    brand = models.ForeignKey(
        Brand,
        related_name='products',
        on_delete=models.PROTECT
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.PROTECT
    )
    description = models.TextField(blank=True, null=True)
    serie_number = models.CharField(max_length=200, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    user_created = models.ForeignKey(
        User,
        related_name='product_created_by',
        on_delete=models.PROTECT
    )
    user_updated = models.ForeignKey(
        User,
        related_name='product_updated_by',
        on_delete=models.PROTECT,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
