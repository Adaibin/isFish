# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class Properties(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.IntegerField(default=1)

    # can_index = models.CharField(max_length=32)
    # can_detail = models.CharField(max_length=64)
    # can_modify = models.CharField(max_length=64)

    fields = models.TextField()
    table_ = models.CharField(max_length=16, null=False, blank=False, unique=True)

    create_time = models.DateTimeField(auto_now=True)


admin.site.register(Properties)
