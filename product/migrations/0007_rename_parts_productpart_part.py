# Generated by Django 4.0.8 on 2023-01-10 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productpart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productpart',
            old_name='parts',
            new_name='part',
        ),
    ]