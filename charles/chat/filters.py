import django_filters

from charles.chat.models import ChatRoom


class ChatRoomFilter(django_filters.FilterSet):
    channel_no = django_filters.CharFilter()

    class Meta:
        model = ChatRoom
        fields = ['channel_no']

