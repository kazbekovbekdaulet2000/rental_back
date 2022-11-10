# Generated by Django 4.0.8 on 2022-11-10 21:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0009_rentinhandorder_file_delete_rentinhandinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentinhandorder',
            name='inventories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None),
        ),
    ]
