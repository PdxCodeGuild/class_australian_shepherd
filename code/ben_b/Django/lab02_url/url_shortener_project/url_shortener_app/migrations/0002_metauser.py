# Generated by Django 4.1.1 on 2022-10-05 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='metaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_shortener_app.urllink')),
            ],
        ),
    ]
