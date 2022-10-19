# Generated by Django 4.0.8 on 2022-10-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_order_userbag_userbagitem_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ord_id',
        ),
        migrations.AddField(
            model_name='product',
            name='instruction_video',
            field=models.URLField(blank=True, null=True, verbose_name='Cсылка на инструкцию'),
        ),
    ]