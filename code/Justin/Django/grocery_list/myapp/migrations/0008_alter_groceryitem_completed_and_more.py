# Generated by Django 4.1.1 on 2022-09-28 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_groceryitem_completed_alter_groceryitem_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 28, 1, 59, 12, 823234, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
