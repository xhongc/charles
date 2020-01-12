from django.contrib import admin

from charles.chat.models import ChatRoom


# Register your models here.
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'channel_no']
    list_filter = ['room_name', 'channel_no']
    search_fields = ['room_name', 'channel_no']


admin.site.register(ChatRoom, ChatRoomAdmin)
