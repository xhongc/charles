from rest_framework import serializers, status
from rest_framework.response import Response

from charles.chat.models import UserProfile, ChatLog, ChatRoom


class FriendsSerializers(serializers.Serializer):
    uid = serializers.CharField(required=True)

    def validate_uid(self, u_id):
        request = self._context.get('request')
        friends = UserProfile.objects.filter(unicode_id=u_id).first()
        if friends and u_id != request.user.profile.unicode_id:
            request.user.profile.friends.add(friends)
            request.user.profile.save()
        else:
            raise serializers.ValidationError('添加好友不存在')
        return u_id

    def save(self, **kwargs):
        u_id = self.validated_data.get('uid')
        request = self._context.get('request')
        friends = UserProfile.objects.filter(unicode_id=u_id).first()
        if friends and u_id != request.user.profile.unicode_id:
            request.user.profile.friends.add(friends)
            request.user.profile.save()
        else:
            raise Exception('error')


class ListFriendsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PostChatLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatLog
        fields = '__all__'


class ListChatLogSerializers(serializers.ModelSerializer):
    chat_datetime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ChatLog
        fields = '__all__'


class ChatRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
