# Generated by Django 2.0.9 on 2018-11-07 18:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20181107_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='foto',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagen'),
        ),
    ]