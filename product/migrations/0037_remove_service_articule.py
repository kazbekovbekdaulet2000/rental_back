# Generated by Django 4.0.8 on 2022-10-14 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_remove_product_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='articule',
        ),
    ]