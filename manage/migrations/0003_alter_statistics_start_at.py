# Generated by Django 4.0.8 on 2022-11-06 06:45

from django.db import migrations, models
import manage.models.stats


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0002_statistics_end_at_statistics_start_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='start_at',
            field=models.DateTimeField(default=manage.models.stats.now_minus_30),
        ),
    ]