# Generated by Django 4.2.11 on 2024-06-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardss',
            name='coordinates',
            field=models.CharField(blank=True, max_length=15000, null=True, verbose_name='Координаты 2GIS'),
        ),
        migrations.AlterField(
            model_name='cardss',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/deps/media', verbose_name='Изображение'),
        ),
    ]