# Generated by Django 4.1.1 on 2022-10-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0002_rename_testfield_metauser_urllink'),
    ]

    operations = [
        migrations.AddField(
            model_name='metauser',
            name='meta',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
