# Generated by Django 4.0.8 on 2022-12-19 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_remove_clientpassportindividual_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientpassportlegal',
            old_name='iin',
            new_name='bin',
        ),
    ]