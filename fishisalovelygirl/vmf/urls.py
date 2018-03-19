# -*- coding: utf-8 -*-

from django.urls import path, include

urlpatterns = [
    path(r'properties/', include('vmf.properties.urls')),
    path(r'user/', include('vmf.user.urls')),
    path(r'group/', include('vmf.group.urls')),
]

