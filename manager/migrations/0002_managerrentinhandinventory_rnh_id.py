# Generated by Django 4.0.8 on 2022-11-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerrentinhandinventory',
            name='rnh_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]