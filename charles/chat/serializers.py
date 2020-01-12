from rest_framework import serializers, status
from rest_framework.response import Response

from charles.chat.models import UserProfile


class FriendsSerializers(serializers.Serializer):
    uid = serializers.CharField(required=True)

    def save(self, **kwargs):
        u_id = self.validated_data.get('uid')
        request = self._context.get('request')
        friends = UserProfile.objects.filter(unicode_id=u_id).first()
        if friends and u_id != request.user.profile.unicode_id:
            request.user.profile.friends.add(friends)
            request.user.profile.save()
        else:
            pass


class ListFriendsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
