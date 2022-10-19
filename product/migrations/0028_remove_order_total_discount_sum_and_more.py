# Generated by Django 4.0.8 on 2022-10-13 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_alter_attribute_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_discount_sum',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_sum',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('count', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
    ]
