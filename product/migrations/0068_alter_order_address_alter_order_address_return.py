# Generated by Django 4.0.8 on 2022-12-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0067_order_address_return_userbag_delivery_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_return',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес возврата'),
        ),
    ]