# Generated by Django 5.0.3 on 2024-04-24 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.supplier'),
        ),
    ]
