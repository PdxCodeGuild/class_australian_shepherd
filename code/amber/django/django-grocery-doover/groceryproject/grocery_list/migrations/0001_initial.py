# Generated by Django 4.1.1 on 2022-09-29 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groceryitem', models.CharField(max_length=200)),
                ('dateadded', models.DateTimeField(default=django.utils.timezone.now)),
                ('todo', models.BooleanField(null=True)),
            ],
        ),
    ]