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



from dwebsocket.decorators import accept_websocket, require_websocket
from collections import defaultdict

# 保存所有接入的用户地址
allconn = defaultdict(list)


@accept_websocket
def echo(request, userid):
    allresult = {}
    # 获取用户信息
    userinfo = request.user
    allresult['userinfo'] = userinfo
    # 声明全局变量
    global allconn
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'chat.html', allresult)
    else:
        # 将链接(请求？)存入全局字典中
        allconn[str(userid)] = request.websocket
        # 遍历请求地址中的消息
        for message in request.websocket:
            # 将信息发至自己的聊天框
            request.websocket.send(message)
            # 将信息发至其他所有用户的聊天框
            for i in allconn:
                if i != str(userid):
                    allconn[i].send(message)
