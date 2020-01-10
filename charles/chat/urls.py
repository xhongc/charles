from django.urls import path
from rest_framework.routers import DefaultRouter

from charles.chat.views import ChatIndexViewsets
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
