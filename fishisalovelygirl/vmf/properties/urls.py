# -*- coding: utf-8 -*-
from django.urls import path

from vmf.properties import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
