# Generated by Django 4.1.1 on 2022-09-27 01:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_myauthor_mymodel_item_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 1, 32, 23, 897408, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]