from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_role = (
        ('Employee', 'Employee'),
        ('Project Manager', 'Project Manager'),
    )
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=user_role)
