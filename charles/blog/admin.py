import xadmin
from charles.blog.models import Category, Tag, Post


class CategoryAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class TagAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class PostAdmin(object):
    list_display = ['title', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author', 'views']
    list_filter = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author', 'views']
    search_fields = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author', 'views']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)
