# Generated by Django 4.1.1 on 2022-09-24 04:11

import datetime
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
                ('myfield', models.CharField(max_length=200)),
                ('mytime', models.DateTimeField(default=datetime.datetime(2022, 9, 24, 4, 11, 15, 740146, tzinfo=datetime.timezone.utc), null=True)),
                ('myboolean', models.BooleanField()),
            ],
        ),
    ]
