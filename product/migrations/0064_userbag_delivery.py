# Generated by Django 4.0.8 on 2022-11-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0063_productdiscount_productitemdiscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbag',
            name='delivery',
            field=models.BooleanField(default=False),
        ),
    ]
