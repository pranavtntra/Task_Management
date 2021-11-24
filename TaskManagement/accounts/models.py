from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

Designation = (
    ("Project Manager", "Project Manager"),
    ("Employee", "Employee"),
)


class Technology(models.Model):
    """ for technologies """
    tech_name = models.CharField(max_length=122, null=True, blank=True)

    def __str__(self):
        return str(self.tech_name)


class User(AbstractUser):
    """Abstract User table"""
    first_name = models.CharField(max_length=122, null=True, blank=True)
    last_name = models.CharField(max_length=122, null=True, blank=True)
    contact = PhoneNumberField()
    designation = models.CharField(
        max_length=50, choices=Designation, null=True, blank=True
    )
    technologies = models.ManyToManyField(Technology, through='IntermediateUserTech')
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name)


class IntermediateUserTech(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    technologies = models.ForeignKey(Technology, on_delete=models.CASCADE)
    topic = models.TextField()

    def __str__(self):
        return  str(self.user_name)
