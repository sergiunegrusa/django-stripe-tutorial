# Generated by Django 4.0.6 on 2022-07-18 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_stipe_price_id_price_stripe_price_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='price',
            new_name='cents',
        ),
    ]
