# Generated by Django 4.0.8 on 2022-12-21 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_inventorytarif_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventorytarif',
            unique_together={('default', 'inventory', 'price')},
        ),
    ]
