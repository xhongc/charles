"""charles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin

from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles import views
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from charles.navi.views import NanaCategoryViewsets, NanaViewsets
from charles.shorturl.views import ShortUrlViewsets
from project.views import ProjectViewset, HeroesViewset, PDFstreamViewsets
from utils.channelsmiddleware import LoginObtainJSONWebToken

router = DefaultRouter()
router.register(r'project', viewset=ProjectViewset, basename='project')
router.register(r'heroes', viewset=HeroesViewset, basename='heroes')
router.register(r'shorturl', viewset=ShortUrlViewsets, basename='shorturl')
router.register(r'nana', viewset=NanaCategoryViewsets, basename='nana')
router.register(r'nana_log', viewset=NanaViewsets, basename='nana_log')
router.register(r'g_pdf', viewset=PDFstreamViewsets, basename='g_pdf')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='API & Dog', description='API文档', public=True)),
    url(r'^api-token-auth/', LoginObtainJSONWebToken.as_view()),
    url(r'blog/', include('charles.blog.urls')),
    url(r'', include('charles.comments.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('md/', TemplateView.as_view(template_name='markdown/md.html'), name='md'),
    path('pdf_viewer/', TemplateView.as_view(template_name='viewer.html'), name='test'),
    path('xhongc/', TemplateView.as_view(template_name='moyu.html'), name='xhongc'),
    path('jsonp/', TemplateView.as_view(template_name='jsonp/json_parse.html'), name='jsonp'),
    path('shorturl/', TemplateView.as_view(template_name='shorturl.html'), name='shorturl'),
    path('generateid/', TemplateView.as_view(template_name='generateid.html'), name='generateid'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^src/(?P<path>.*)$', views.serve),
    ]
