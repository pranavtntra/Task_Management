from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    user_role = (
        ('Admin', 'Admin'),
        ('Project Manager', 'Project Manager'),
        ('Employee', 'Employee'),
    )
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    role = models.CharField(max_length=20, choices=user_role)

    # def __str__(self):
    #     return(self.first_name)
