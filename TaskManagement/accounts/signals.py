from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from accounts.models import User
from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from TaskManagement.settings import EMAIL_HOST_USER
from accounts.constants import SIGNUP_MESSAGES, SIGNUP_SUBJECT

SUBJECT = SIGNUP_SUBJECT
MESSAGES = SIGNUP_MESSAGES



@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = User.objects.get(email=email_address.email)
    user.email_verified = True
    user.save()


@receiver(post_save, sender=User)
def mail_send(sender, instance, **kwargs):
    if kwargs['created'] and instance.email_verified:
        send_mail(
            SUBJECT,
            MESSAGES,
            EMAIL_HOST_USER,
            [instance.email],
        )
