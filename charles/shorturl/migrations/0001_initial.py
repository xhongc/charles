# Generated by Django 2.0.3 on 2019-12-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('short_link', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('paste_path', models.CharField(max_length=255)),
            ],
        ),
    ]
