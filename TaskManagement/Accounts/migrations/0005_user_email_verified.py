# Generated by Django 3.2.5 on 2021-07-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_remove_user_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
