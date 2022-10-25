# Generated by Django 4.1.2 on 2022-10-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=666),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=69),
        ),
    ]