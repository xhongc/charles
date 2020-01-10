from django.db import models
from django.utils import timezone


# Create your models here.

class Project(models.Model):
    offer_title = models.CharField(blank=True, max_length=10, null=True)
    status = models.CharField(blank=True, max_length=10, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)


class Heroes(models.Model):
    name = models.CharField(blank=True, max_length=255, null=True)
