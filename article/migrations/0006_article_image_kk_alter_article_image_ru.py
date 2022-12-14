# Generated by Django 4.0.8 on 2022-11-16 05:08

import article.models.article
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_rename_image_article_image_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_kk',
            field=models.ImageField(null=True, upload_to=article.models.article.image_dir, verbose_name='Фото(каз)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_ru',
            field=models.ImageField(upload_to=article.models.article.image_dir, verbose_name='Фото(рус)'),
        ),
    ]
