# Generated by Django 5.0.3 on 2024-04-24 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_supplier_product_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
    ]
