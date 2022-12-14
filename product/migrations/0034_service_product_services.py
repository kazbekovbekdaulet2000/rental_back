# Generated by Django 4.0.8 on 2022-10-14 08:27

import ckeditor_uploader.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_alter_botuser_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_kk', models.CharField(max_length=255)),
                ('articule', models.CharField(max_length=255, unique=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_kk', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('daily_price', models.IntegerField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
                'ordering': ('created_at',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, to='product.service'),
        ),
    ]
