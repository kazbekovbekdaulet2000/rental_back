# Generated by Django 4.0.8 on 2022-11-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_image_kk_alter_article_image_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='outer_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]