# Generated by Django 4.0.8 on 2023-01-10 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_parts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parts',
        ),
    ]