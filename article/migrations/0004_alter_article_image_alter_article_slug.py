# Generated by Django 4.0.8 on 2022-11-14 15:34

import article.models.article
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=article.models.article.image_dir, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=5196, null=True, unique=True),
        ),
    ]