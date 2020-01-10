from django.contrib import admin
from .models import Project


# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ["status", "offer_title"]


admin.site.register(Project, PeopleAdmin)
