# Generated by Django 2.1 on 2019-05-10 07:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king', '0005_auto_20190510_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tel',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^[09]\\d{9,10}$')]),
        ),
    ]
