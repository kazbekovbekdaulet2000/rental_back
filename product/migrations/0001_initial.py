# Generated by Django 4.1.1 on 2022-09-30 11:12

import ckeditor_uploader.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_kk', models.CharField(max_length=255)),
                ('icon', models.FileField(upload_to='category_icon')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_kk', models.CharField(max_length=255)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_kk', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('daily_price', models.IntegerField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('image', models.ImageField(blank=True, upload_to='products', verbose_name='Фото')),
                ('image_thumb360', models.ImageField(blank=True, max_length=500, null=True, upload_to='products', verbose_name='Фото (480px)')),
                ('image_thumb720', models.ImageField(blank=True, max_length=500, null=True, upload_to='products', verbose_name='Фото (720px)')),
                ('image_thumb1080', models.ImageField(blank=True, max_length=500, null=True, upload_to='products', verbose_name='Фото (1080px)')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-created_at'],
            },
        ),
    ]
