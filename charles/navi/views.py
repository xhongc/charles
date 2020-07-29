# Create your views here.
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from charles.navi.models import Category, Nana
from charles.navi.serializers import ListNanaCategorySerializers, NanaLogSerializer
import time


class NanaCategoryViewsets(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ListNanaCategorySerializers

    def get_queryset(self):
        return Category.objects.order_by('ordering')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        for each in serializer.data:
            each['cates'].sort(key=lambda x: x.get('read_no'), reverse=True)

        return Response(serializer.data)


class NanaViewsets(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Nana.objects.all()
    serializer_class = NanaLogSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_no = instance.read_no + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
