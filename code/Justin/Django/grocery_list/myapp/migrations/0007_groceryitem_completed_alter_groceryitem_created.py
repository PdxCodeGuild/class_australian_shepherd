# Generated by Django 4.1.1 on 2022-09-27 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_groceryitem_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 2, 23, 34, 321524, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]