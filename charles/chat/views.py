from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from charles.chat.filters import ChatRoomFilter
from charles.chat.models import ChatRoom, ChatLog
from charles.chat.serializers import FriendsSerializers, ListFriendsSerializers, PostChatLogSerializers, \
    ChatRoomSerializers, ListChatLogSerializers, ListChatRoomSerializers, UpdateChatRoomSerializers
from utils.base_serializer import BasePagination


@login_required(login_url='/login/')
def index(request):
    friends = request.user.profile.friends.all()
    return render(request, 'chat/boot_chat.html', locals())


class ChatIndexViewsets(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def list(self, request, *args, **kwargs):
        return render(request, template_name='chat/boot_chat.html')


class FriendsViewsets(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = FriendsSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        channel_no = self.request.query_params.get('channel_no', None)
        if channel_no:
            return self.request.user.profile.friends.exclude(chat_member__channel_no=channel_no).exclude(
                chat_admins__channel_no=channel_no)
        return self.request.user.profile.friends.all('')

    def get_serializer_class(self):
        if self.action == 'create':
            serializer_class = FriendsSerializers
        elif self.action == 'list':
            serializer_class = ListFriendsSerializers
        else:
            raise Exception('no such method')
        return serializer_class


class ChatLogViewsets(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = BasePagination

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return ListChatLogSerializers
        return ListChatLogSerializers

    def get_queryset(self):
        start = datetime.now().date()
        end = start + timedelta(days=1)
        return ChatLog.objects.filter(said_to_room__channel_no=self.request.query_params.get('channel_no'),
                                      chat_datetime__range=(start, end)).order_by('-chat_datetime')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data[::-1])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ChatRoomViewsets(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, GenericViewSet):
    """
        list:
        查看房间信息成员和创建者
        create:
        创建房间
        retrieve:
        查看特定房间号信息
        update:
        邀请好友到该房间
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ChatRoomFilter
    lookup_field = 'channel_no'

    def get_queryset(self):
        channel_no = self.request.query_params.get('channel_no', None)
        if channel_no:
            return ChatRoom.objects.filter(channel_no=channel_no)
        else:
            return ChatRoom.objects.filter(Q(admins=self.request.user.profile) | Q(members=self.request.user.profile)).distinct().order_by('ordering')

    def get_serializer_class(self):
        if self.action == 'list':
            return ListChatRoomSerializers
        elif self.action == 'update':
            return UpdateChatRoomSerializers
        return ChatRoomSerializers
