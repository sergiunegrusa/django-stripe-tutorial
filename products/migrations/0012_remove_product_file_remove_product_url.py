# Generated by Django 4.0.6 on 2022-07-18 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_file_product_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
    ]
