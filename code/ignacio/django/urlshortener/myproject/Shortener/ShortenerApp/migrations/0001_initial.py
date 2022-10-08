# Generated by Django 4.1.1 on 2022-10-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_url', models.CharField(max_length=200)),
                ('long_url', models.URLField(max_length=250)),
            ],
        ),
    ]
