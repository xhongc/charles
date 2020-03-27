from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=64, null=False, blank=False)
    room_description = models.CharField(max_length=255, default='这里还没什么描述')
    img_path = models.CharField(max_length=255, default='/')
    channel_no = models.CharField(max_length=8, null=False, blank=False, unique=True)
    admins = models.ManyToManyField('UserProfile', null=False, blank=False, related_name='chat_admins')
    members = models.ManyToManyField('UserProfile', blank=True, null=True, related_name='chat_member')
    max_number = models.IntegerField(default=5)

    def __str__(self):
        return self.room_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nick_name = models.CharField(max_length=64)
    signature = models.CharField(max_length=255, null=True, blank=True)
    friends = models.ManyToManyField('self', related_name='my_friends', blank=True)
    unicode_id = models.IntegerField(default=-1, blank=False, null=False, unique=True)
    img_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nick_name + ': ' + str(self.unicode_id)

    def get_my_chat_room(self):
        chat_member = self.chat_member.all().values_list('channel_no', flat=True)
        chat_admins = self.chat_admins.all().values_list('channel_no', flat=True)
        return list(chat_member) + list(chat_admins)


class ChatLog(models.Model):
    chat_datetime = models.DateTimeField(null=True, blank=True, db_index=True)
    content = models.TextField(null=True, blank=True)
    msg_type = models.CharField(max_length=16, null=True, blank=True)
    who_said = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, related_name='who_said')
    said_to = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True,
                                related_name='said_to')
    said_to_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True,
                                     related_name='said_to_room')
