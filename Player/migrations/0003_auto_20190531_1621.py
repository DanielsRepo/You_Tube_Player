# Generated by Django 2.1.8 on 2019-05-31 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Player', '0002_likedvideo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedvideo',
            name='user',
        ),
        migrations.AddField(
            model_name='video',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='user_favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
