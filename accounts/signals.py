from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User

@receiver(post_save, sender=User)
def update_user_inactive(sender, instance, created, **kwargs):
    if not instance.is_active:
        User.objects.filter(
            pk=instance.pk
        ).update(
            race_ethnicity=None,
            gender=None
        )
