# -*- coding: utf-8 -*-
from django.http import HttpResponse


def index(request):
    """

    :param request:
    :return:
    """

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
