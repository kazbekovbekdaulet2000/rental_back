# Generated by Django 4.1.1 on 2022-10-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_articule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='articule',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]