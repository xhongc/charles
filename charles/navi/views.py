from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from charles.navi.models import Nana, Category
from charles.navi.serializers import ListNanaCategorySerializers


class NanaCategoryViewsets(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = ListNanaCategorySerializers
