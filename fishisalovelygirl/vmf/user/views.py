# -*- coding: utf-8 -*-
from django.http import HttpResponse
from vmf.user.model import User


def index(request):
    """

    :param request:
    :return:
    """
    user = User.objects.all()
    print(len(user))
    return HttpResponse("Hello, world. You're at the polls index.")


def create(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the polls index.")


def modify(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the polls index.")


def delete(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the polls index.")
