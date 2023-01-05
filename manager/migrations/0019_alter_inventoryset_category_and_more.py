# Generated by Django 4.0.8 on 2022-12-30 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_inventorysetitem_tarif_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryset',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.inventorycategory'),
        ),
        migrations.AlterField(
            model_name='inventoryset',
            name='unique_id',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='inventorysetitem',
            name='tarif_price',
            field=models.IntegerField(),
        ),
    ]
