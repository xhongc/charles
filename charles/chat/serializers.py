import random

from rest_framework import serializers

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
    admins = serializers.CharField(read_only=True)
    channel_no = serializers.CharField(required=False)

    class Meta:
        model = ChatRoom
        fields = '__all__'

    def save(self, **kwargs):
        request = self._context.get('request')
        members = self.validated_data.pop('members')
        self.validated_data['channel_no'] = random.randint(2, 9999)
        ct_room = ChatRoom(**self.validated_data)
        self.validated_data['members'] = members
        ct_room.save()
        ct_room.admins.add(request.user.profile)
        ct_room.save()


class ListChatRoomSerializers(serializers.ModelSerializer):
    admins = ListFriendsSerializers(many=True)
    members = ListFriendsSerializers(many=True)

    class Meta:
        model = ChatRoom
        fields = '__all__'
#todo 加好友 不在群里的 报错ws 不要执行任何

class UpdateChatRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('members',)

    def validate_members(self, attrs):
        return self.initial_data.getlist('members[]')

    def save(self, **kwargs):
        print(self.validated_data)
        print(self.initial_data.getlist('members[]'))
