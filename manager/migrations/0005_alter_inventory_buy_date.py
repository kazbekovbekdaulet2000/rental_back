# Generated by Django 4.0.8 on 2022-11-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_client_clientpassportindividual_clientpassportlegal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='buy_date',
            field=models.DateField(null=True),
        ),
    ]
