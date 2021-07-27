from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
import datetime
from phonenumber_field.modelfields import PhoneNumberField

# from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    roles = (
        ('admin', 'Admin'),
         ('manager', 'Project Manager'),
         ('employee', 'Employee')
     )
    
    contact = PhoneNumberField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50, choices=roles)
    allocation = models.IntegerField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)


    def __str__(self):
        
        return str(self.name)



