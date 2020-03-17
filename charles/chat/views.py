from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from charles.chat.models import ChatRoom, ChatLog
from charles.chat.serializers import FriendsSerializers, ListFriendsSerializers, PostChatLogSerializers


@login_required(login_url='/login/')
def index(request):
    char_rooms = ChatRoom.objects.all()
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
        return self.request.user.profile.friends.all()
        # return User.objects.get(username='admin').profile.friends.all()

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
    serializer_class = PostChatLogSerializers

    def get_queryset(self):
        return ChatLog.objects.filter()
