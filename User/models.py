from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        ('User', 'User'),
        ('Admin', 'Admin'),
    )
    status = models.CharField(max_length=6, choices=STATUS, default='User')
