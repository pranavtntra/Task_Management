# Generated by Django 3.2.5 on 2021-07-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210726_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='Designation',
        ),
    ]
