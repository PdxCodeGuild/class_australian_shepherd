# Generated by Django 4.1.1 on 2022-09-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='author',
            field=models.CharField(default='n/a', max_length=150),
        ),
    ]
