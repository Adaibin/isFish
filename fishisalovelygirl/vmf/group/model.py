# -*- coding: utf-8 -*-
from django.db import models


class Group(models.Model):
    """Group
    """

    id = models.AutoField(primary_key=True)
    version = models.IntegerField(default=1)

    name = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now=True)
