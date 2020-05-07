import xadmin
from .models import Project


# Register your models here.

class PeopleAdmin(object):
    list_display = ["id", "offer_title", "relative_url", 'date_created', 'popular_ordering']


xadmin.site.register(Project, PeopleAdmin)
