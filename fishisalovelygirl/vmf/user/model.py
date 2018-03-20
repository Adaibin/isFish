# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    """User
    """

    id = models.AutoField(primary_key=True)
    version = models.IntegerField(default=1)

    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)
