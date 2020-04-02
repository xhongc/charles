import django_filters

from charles.chat.models import ChatRoom, ChatLog


class ChatRoomFilter(django_filters.FilterSet):
    channel_no = django_filters.CharFilter()

    class Meta:
        model = ChatRoom
        fields = ['channel_no']


class ChatLogFilter(django_filters.FilterSet):
    said_to_room__channel_no = django_filters.CharFilter()

    class Meta:
        model = ChatLog
        fields = ['said_to_room__channel_no']
