# Generated by Django 4.1.1 on 2022-09-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo_list",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("objective", models.TextField(max_length=400)),
                ("start_date", models.DateTimeField()),
                ("in_progress", models.BooleanField()),
            ],
        ),
    ]