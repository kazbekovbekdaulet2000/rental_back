# Generated by Django 4.0.8 on 2022-11-14 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0058_product_rnh_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('order', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Новый продукт',
                'verbose_name_plural': 'Новые продукты',
                'ordering': ('created_at',),
            },
        ),
    ]
