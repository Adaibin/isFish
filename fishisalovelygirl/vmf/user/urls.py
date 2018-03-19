# -*- coding: utf-8 -*-
from django.urls import path

from vmf.user import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/', views.index, name='detail'),
    path('create/', views.index, name='create'),
    path('modify/', views.index, name='modify'),
    path('delete/', views.index, name='delete'),
]
