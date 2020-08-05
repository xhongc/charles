from django.db import models


# Create your models here.

class ShortUrl(models.Model):
    short_link = models.CharField(primary_key=True, max_length=7, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    paste_path = models.CharField(max_length=255, null=False)
