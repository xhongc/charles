# Generated by Django 2.2.3 on 2019-08-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190708_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
