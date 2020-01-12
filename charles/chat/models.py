from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=64, null=False, blank=False)
    room_description = models.CharField(max_length=255, null=False, blank=False)
    img_path = models.CharField(max_length=255, null=False, blank=False)
    channel_no = models.CharField(max_length=8, null=False, blank=False)
    admins = models.ManyToManyField('UserProfile', blank=True, related_name='chat_admins')
    members = models.ManyToManyField('UserProfile', blank=True, related_name='chat_member')
    max_number = models.IntegerField(default=5)

    def __str__(self):
        return self.room_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    nick_name = models.CharField(max_length=64)
    signature = models.CharField(max_length=255, null=True, blank=True)
    friends = models.ManyToManyField('self', related_name='my_friends', blank=True)
    unicode_id = models.IntegerField(default=-1, blank=False, null=False, unique=True)

    def __str__(self):
        return self.nick_name
