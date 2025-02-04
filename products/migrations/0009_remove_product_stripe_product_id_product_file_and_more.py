# Generated by Django 4.0.6 on 2022-07-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_cents_price_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stripe_product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='product_files/'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(default=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
