import requests
import io

import requests
from django.conf import settings
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from qiniu import Auth
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from charles.navi.models import Nana
from project.filters import ProjectFilter
from project.serializers import ProjectSerializers, HeroesSerializers
from .models import Project, Heroes
from .tasks import catch_home_task


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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        catch_home_task.delay()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PDFstreamViewsets(mixins.ListModelMixin, GenericViewSet):
    def list(self, request, *args, **kwargs):
        url = request.query_params.get('pdfurl', None)
        if not url:
            return JsonResponse({'status': '0000'})
        try:
            r = requests.get(url, stream=True)
        except:
            r = ''
        fd = io.BytesIO()
        for chunk in r.iter_content(2000):
            fd.write(chunk)
        return StreamingHttpResponse(streaming_content=(fd.getvalue(),), content_type='application/octet-stream')


@csrf_exempt
def QiniuCallback(request):
    """七牛回调"""
    origin_authorization = request.META.get('HTTP_AUTHORIZATION', '') or ''
    callback_url = settings.QINNIU_CALLBACK_URL
    filename = request.POST.get('filename', '')
    filesize = request.POST.get('filesize', '')
    uid = request.POST.get('uid', '')

    callback_body = f'filename={filename}&filesize={filesize}&uid={uid}'
    if origin_authorization:
        is_qiniu_callback = Auth(settings.QINIU_ACCESS_KEY, settings.QINNIU_SECRET_KEY).verify_callback(
            origin_authorization, callback_url, callback_body)
        if is_qiniu_callback:
            print(uid, '成功')
            cdn_url = settings.CDN_URL + uid
            Nana.objects.filter(id=uid).update(img_path=cdn_url)

    return JsonResponse({"success": True, "name": filename})
