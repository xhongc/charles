from django.db import models


# Create your models here.

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=64, null=False, blank=False)
    room_description = models.CharField(max_length=255, null=False, blank=False)
    img_path = models.CharField(max_length=255, null=False, blank=False)
    channel_no = models.CharField(max_length=8, null=False, blank=False)
