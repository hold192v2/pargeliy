# Generated by Django 4.2.11 on 2024-05-15 19:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating_app', '0003_post_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Comment',
        ),
    ]
