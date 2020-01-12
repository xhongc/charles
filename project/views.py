import json
import time

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
from rest_framework.viewsets import ModelViewSet

from project.filters import ProjectFilter
from project.serializers import ProjectSerializers, HeroesSerializers
from .models import Project, Heroes
from .tasks import add
from django.db import connection
from django.shortcuts import render


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


class ProjectViewset(ModelViewSet):
    """
    list:
        项目详情
    create:
        创建项目
    destroy:
        删除项目
    """
    # 查询集
    queryset = Project.objects.all()
    # 序列化
    serializer_class = ProjectSerializers
    # 分页
    pagination_class = ProjectPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter

    def update(self, request, *args, **kwargs):
        print('ok')
        res = add.delay(4, 4)
        print(res)
        return Response({'code': '1234'})


class HeroesViewset(ModelViewSet):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializers



