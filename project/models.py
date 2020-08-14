from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Project(models.Model):
    offer_title = models.CharField(blank=True, max_length=64, null=True)
    sub_title = models.CharField(blank=True, max_length=255, null=True)
    introduction = models.CharField(blank=True, max_length=255, null=True)
    logo_img = models.CharField(blank=True, max_length=255, null=True)
    status = models.CharField(blank=True, max_length=10, null=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(auto_now=True)
    relative_url = models.CharField(blank=True, max_length=64, null=True)
    common_ordering = models.IntegerField(default=1)
    popular_ordering = models.IntegerField(default=1)


class Heroes(models.Model):
    name = models.CharField(blank=True, max_length=255, null=True)
