# Generated by Django 3.2.8 on 2022-01-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211206_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='activepause',
            name='slug',
            field=models.SlugField(default=1, max_length=150, verbose_name='Ruta Web'),
            preserve_default=False,
        ),
    ]
