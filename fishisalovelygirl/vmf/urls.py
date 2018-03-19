# -*- coding: utf-8 -*-

from django.urls import path, include

urlpatterns = [
    path(r'properties/', include('vmf.properties.urls')),
]

