# Generated by Django 4.0.8 on 2023-01-10 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_parts'),
        ('manager', '0021_inventorytariftimeperiod_inventorytarif_time_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequestinventory',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
    ]