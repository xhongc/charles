from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import mixins

# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from charles.shorturl.models import ShortUrl
from charles.shorturl.serializers import ShortUrlCreateSerilizer


class ShortUrlViewsets(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    create:
        创建URL 短链接
    retrieve:
        根据id 跳转 短链接
    """
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlCreateSerilizer
    throttle_classes = [UserRateThrottle]

    def get_authentication_classes(self):
        if self.action == 'create':
            authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
        else:
            authentication_classes = ''
        return authentication_classes

    def get_permission_classes(self):
        if self.action == 'create':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = ''
        return permission_classes

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return HttpResponseRedirect(serializer.data.get('paste_path'))


class IndexViewsets(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def list(self, request, *args, **kwargs):
        return render(request, template_name='index.html')
