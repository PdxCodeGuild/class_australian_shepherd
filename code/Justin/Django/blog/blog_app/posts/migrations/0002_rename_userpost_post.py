# Generated by Django 4.1.1 on 2022-10-13 02:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPost',
            new_name='Post',
        ),
    ]
