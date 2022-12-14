# Generated by Django 4.1.1 on 2022-09-27 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_mymodel_active_alter_mymodel_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('requestor', models.CharField(max_length=200, null=True)),
                ('item_description', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 9, 27, 2, 11, 14, 442595, tzinfo=datetime.timezone.utc), null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
