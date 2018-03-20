# -*- coding: utf-8 -*-
from django.urls import path

from vmf.user import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('modify/', views.modify, name='modify'),
    path('delete/', views.delete, name='delete'),
]
