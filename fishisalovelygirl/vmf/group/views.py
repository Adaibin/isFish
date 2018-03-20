# -*- coding: utf-8 -*-
from django.http import HttpResponse
from vmf.group.model import Group


def index(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("group index.")


def create(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("group create.")


def detail(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("group detail.")


def modify(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("group modify.")


def delete(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("group delete.")
