# Generated by Django 2.1.8 on 2019-05-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LikedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200, null=True)),
                ('video_title', models.CharField(max_length=200, null=True)),
                ('channel_title', models.CharField(max_length=200, null=True)),
                ('preview', models.CharField(max_length=200, null=True)),
                ('query', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
