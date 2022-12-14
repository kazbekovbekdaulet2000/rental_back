# Generated by Django 4.1.1 on 2022-09-30 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='category_icon'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
