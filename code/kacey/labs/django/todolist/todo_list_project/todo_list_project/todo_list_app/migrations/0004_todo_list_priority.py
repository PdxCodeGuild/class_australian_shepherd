# Generated by Django 4.1.1 on 2022-10-04 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list_app", "0003_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo_list",
            name="priority",
            field=models.CharField(default="Low", max_length=100),
        ),
    ]
