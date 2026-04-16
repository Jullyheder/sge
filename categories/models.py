from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    user_created = models.ForeignKey(
        User,
        related_name='categories_created_by',
        on_delete=models.PROTECT
    )
    user_updated = models.ForeignKey(
        User,
        related_name='categories_updated_by',
        on_delete=models.PROTECT,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name
