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
    return HttpResponse("user index.")


def create(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("user create.")


def detail(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("user detail.")


def modify(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("user modify.")


def delete(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("user delete.")
