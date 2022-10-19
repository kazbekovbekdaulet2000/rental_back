# Generated by Django 4.0.8 on 2022-10-13 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_order_bag_order_first_time_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbag',
            name='previous_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.userbag'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]