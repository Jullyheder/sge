from django.db import models


class AIResult(models.Model):
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AI Result'
        verbose_name_plural = 'AI Results'
        ordering = ['-created_at']

    def __str__(self):
        return f'AIResult {self.id} - {self.created_at}'
