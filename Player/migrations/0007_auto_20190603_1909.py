# Generated by Django 2.1.8 on 2019-06-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0006_auto_20190603_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='throughmodel',
            name='queries',
        ),
        migrations.RemoveField(
            model_name='throughmodel',
            name='videos',
        ),
        migrations.RemoveField(
            model_name='video',
            name='query',
        ),
        migrations.AddField(
            model_name='video',
            name='query',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Query',
        ),
        migrations.DeleteModel(
            name='ThroughModel',
        ),
    ]
