from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

Role = (
        ('Project Manager', 'Project Manager'),
        ('Employee', 'Employee'),
    )

class User(AbstractUser):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    contact =  PhoneNumberField()
    role = models.CharField(max_length =50, choices=Role)

    def __str__(self):
        return self.first_name