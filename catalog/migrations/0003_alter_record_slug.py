# Generated by Django 4.1.5 on 2023-01-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
        ),
    ]
