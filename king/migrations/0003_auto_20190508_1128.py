# Generated by Django 2.1 on 2019-05-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king', '0002_auto_20190508_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]
