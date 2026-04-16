from django.db import models
from django.contrib.auth.models import AbstractUser


RACE_ETHNICITY_CHOICES = [
    ('WHITE', 'Branco'),
    ('BLACK', 'Negro'),
    ('HISPANIC', 'Hispano'),
    ('ASIAN', 'Asiático'),
    ('OTHER', 'Outro'),
]

GENDER_CHOICES = [
    ('MALE', 'Masculino'),
    ('FEMALE', 'Feminino'),
    ('OTHER', 'Outro'),
]


class User(AbstractUser):
    position = models.CharField(max_length=255, blank=True, null=True)
    race_ethnicity = models.CharField(
        max_length=100,
        choices=RACE_ETHNICITY_CHOICES,
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=100,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
