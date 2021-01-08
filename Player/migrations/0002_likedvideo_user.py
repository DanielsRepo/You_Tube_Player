# Generated by Django 2.1.8 on 2019-05-31 12:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likedvideo',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
