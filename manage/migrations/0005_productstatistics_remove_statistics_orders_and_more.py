# Generated by Django 4.0.8 on 2022-11-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0057_alter_botuser_user_id'),
        ('manage', '0004_statistics_orders_alter_statistics_start_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': None,
            },
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='orders',
        ),
        migrations.AddField(
            model_name='statistics',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='start_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='ProductCountStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_days_count', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
            options={
                'db_table': None,
            },
        ),
    ]