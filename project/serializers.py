from django.db.models import F
from rest_framework import serializers

from project.models import Project, Heroes


class ProjectSerializers(serializers.ModelSerializer):
    offer_title = serializers.CharField(required=False, label='名称', help_text='项目包名称')
    status = serializers.CharField(required=False, label='status',
                                   error_messages={'required': '请输入状态'},
                                   help_text='项目包状态')

    def save(self, **kwargs):
        self.instance.popular_ordering = self.instance.popular_ordering + 1
        self.instance.save()

    class Meta:
        model = Project
        fields = '__all__'


class HeroesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = '__all__'
