# Generated by Django 4.0.8 on 2022-11-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0010_rentinhandorder_inventories'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentInHandInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5192)),
                ('amount_rent_sum', models.BigIntegerField(null=True)),
                ('price', models.BigIntegerField()),
            ],
        ),
    ]
