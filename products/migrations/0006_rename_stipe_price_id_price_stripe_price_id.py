# Generated by Django 4.0.6 on 2022-07-18 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_price_product_stripe_product_id_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='stipe_price_id',
            new_name='stripe_price_id',
        ),
    ]