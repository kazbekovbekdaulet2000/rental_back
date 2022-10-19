# Generated by Django 4.0.8 on 2022-10-08 15:34

from django.db import migrations, models
import product.models.product_photo


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_productphoto_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='image',
            field=models.ImageField(blank=True, upload_to=product.models.product_photo.thumb_dir, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='image_thumb1080',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=product.models.product_photo.thumb_dir, verbose_name='Фото (1080px)'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='image_thumb360',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=product.models.product_photo.thumb_dir, verbose_name='Фото (480px)'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='image_thumb720',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=product.models.product_photo.thumb_dir, verbose_name='Фото (720px)'),
        ),
    ]
