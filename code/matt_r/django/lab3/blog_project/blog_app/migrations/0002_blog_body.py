# Generated by Django 4.1.2 on 2022-10-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(max_length=200, null=True),
        ),
    ]