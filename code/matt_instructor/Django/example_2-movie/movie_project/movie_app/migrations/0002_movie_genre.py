# Generated by Django 4.1.1 on 2022-09-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]