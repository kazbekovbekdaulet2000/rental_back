# Generated by Django 4.0.8 on 2022-11-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0060_alter_productannouncement_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rnh_ids',
        ),
        migrations.AddField(
            model_name='product',
            name='rnh_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]