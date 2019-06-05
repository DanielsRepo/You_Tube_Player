# Generated by Django 2.1.8 on 2019-06-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0007_auto_20190603_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='query',
        ),
        migrations.AddField(
            model_name='video',
            name='query',
            field=models.ManyToManyField(blank=True, to='Player.Query'),
        ),
    ]
