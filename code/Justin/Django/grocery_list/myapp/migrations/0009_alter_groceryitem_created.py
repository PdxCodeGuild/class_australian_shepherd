# Generated by Django 4.1.1 on 2022-09-29 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_groceryitem_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 2, 7, 9, 425945, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]