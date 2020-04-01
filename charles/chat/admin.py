import xadmin
from charles.chat.models import ChatRoom, ChatLog, UserProfile
from xadmin import views


# Register your models here.
class ChatRoomAdmin(object):
    list_display = ['room_name', 'channel_no']
    list_filter = ['room_name', 'channel_no']
    search_fields = ['room_name', 'channel_no']


class ChatLogAdmin(object):
    list_display = ['chat_datetime', 'content']
    list_filter = ['who_said', 'said_to', 'said_to_room']


class UserProfileAdmin(object):
    list_display = ['user', 'nick_name', 'unicode_id']


xadmin.site.register(ChatRoom, ChatRoomAdmin)
xadmin.site.register(ChatLog, ChatLogAdmin)
xadmin.site.register(UserProfile, UserProfileAdmin)


class GlobalSettings(object):
    site_title = "少年与白"
    site_footer = "Copyright 2020"


xadmin.site.register(views.CommAdminView, GlobalSettings)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
