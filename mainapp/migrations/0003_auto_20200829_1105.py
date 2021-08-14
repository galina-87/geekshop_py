# Generated by Django 2.2 on 2020-08-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200829_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='{% static "img/logo.png" %}', upload_to='prodacts_photo', verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_descr',
            field=models.CharField(blank=True, max_length=64, verbose_name='краткое описание товара'),
        ),
    ]