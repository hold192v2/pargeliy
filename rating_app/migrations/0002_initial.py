# Generated by Django 4.2.11 on 2024-05-15 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rating_app', '0001_initial'),
        ('map', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.cardss'),
        ),
    ]