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

xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles import views
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from charles.chat.views import FriendsViewsets, ChatLogViewsets, ChatRoomViewsets
from charles.shorturl.views import ShortUrlViewsets
from project.views import ProjectViewset, HeroesViewset
from utils.channelsmiddleware import LoginObtainJSONWebToken

router = DefaultRouter()
router.register(r'project', viewset=ProjectViewset, base_name='project')
router.register(r'heroes', viewset=HeroesViewset, base_name='heroes')
router.register(r'shorturl', viewset=ShortUrlViewsets, base_name='shorturl')
router.register(r'friends', viewset=FriendsViewsets, base_name='friends')
router.register(r'chat_log', viewset=ChatLogViewsets, base_name='chat_log')
router.register(r'chat_room', viewset=ChatRoomViewsets, base_name='chat_room')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^admin/', admin.site.urls),
    url('^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='API & Dog', description='API文档', public=True)),
    url(r'^api-token-auth/', LoginObtainJSONWebToken.as_view()),
    url(r'blog/', include('charles.blog.urls')),
    url(r'', include('charles.comments.urls')),
    path('chat/', include('charles.chat.urls'), name='chat-url'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('md/', TemplateView.as_view(template_name='markdown/md.html'), name='md'),
    path('jsonp/', TemplateView.as_view(template_name='jsonp/json_parse.html'), name='jsonp'),
    path('bc/', TemplateView.as_view(template_name='chat/boot_chat.html'), name='bc'),
    path('shorturl/', TemplateView.as_view(template_name='shorturl.html'), name='shorturl'),
    path('generateid/', TemplateView.as_view(template_name='generateid.html'), name='generateid'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^src/(?P<path>.*)$', views.serve),
    ]
