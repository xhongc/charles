import json
import time
import requests
import io

from django.http import HttpResponse
from django.utils.functional import cached_property
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from project.filters import ProjectFilter
from project.serializers import ProjectSerializers, HeroesSerializers
from .models import Project, Heroes
from .tasks import add
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse


class ProjectPagination(PageNumberPagination):
    """
    自定义分页
    """
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class ProjectViewset(mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    """
    list:
        项目详情
    create:
        创建项目
    destroy:
        删除项目
    """
    # 查询集
    queryset = Project.objects.order_by('-popular_ordering')
    # 序列化
    serializer_class = ProjectSerializers
    # 分页
    pagination_class = ProjectPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter


class HeroesViewset(ModelViewSet):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializers


class PDFstreamViewsets(mixins.ListModelMixin, GenericViewSet):
    def list(self, request, *args, **kwargs):
        a = time.time()
        url = request.query_params.get('pdfurl', None)
        if not url:
            return JsonResponse({'status': '0000'})
        r = requests.get(url, stream=True)
        fd = io.BytesIO()
        for chunk in r.iter_content(2000):
            fd.write(chunk)
        print(time.time() - a)
        return StreamingHttpResponse(streaming_content=(fd.getvalue(),), content_type='application/pdf')
