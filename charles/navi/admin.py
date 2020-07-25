import xadmin

from charles.navi.models import Nana, Category


# Register your models here.
class NanaAdmin(object):
    list_display = ['title', 'description', 'url', 'cate']


class NanaCategoryAdmin(object):
    list_display = ['title', 'html_id']


xadmin.site.register(Nana, NanaAdmin)
xadmin.site.register(Category, NanaCategoryAdmin)
