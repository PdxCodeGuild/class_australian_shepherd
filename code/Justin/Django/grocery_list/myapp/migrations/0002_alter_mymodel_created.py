# Generated by Django 4.1.1 on 2022-09-24 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 3, 27, 34, 864333, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]