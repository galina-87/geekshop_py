# Generated by Django 2.2 on 2020-09-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20200830_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='photo',
            field=models.ImageField(default='user_photo/logo.png', upload_to='user_photo'),
        ),
    ]
