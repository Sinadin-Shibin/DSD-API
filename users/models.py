from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    age = models.IntegerField(null=True)
    Gender = (
        (1, 'Male'),
        (2, 'Female')
    )
    gender = models.CharField(null=True,choices=Gender, max_length=1)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

    def __str__(self):
        return self.email

