# Generated by Django 2.1.8 on 2019-06-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0004_delete_likedvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateField(null=True),
        ),
    ]