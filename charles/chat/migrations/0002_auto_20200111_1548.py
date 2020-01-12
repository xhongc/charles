# Generated by Django 2.2.9 on 2020-01-11 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='max_number',
            field=models.IntegerField(default=5),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=64)),
                ('signature', models.CharField(blank=True, max_length=255, null=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='chat.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='chat_admins', to='chat.UserProfile'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='chat_member', to='chat.UserProfile'),
        ),
    ]
