# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.apps import apps
from django.template.response import TemplateResponse


def get_fields(app, model):
    """

    :param app:
    :param model:
    """

    return apps.get_model(app, model)._meta.fields


def index(request):
    """

    :param request:
    :return:
    """

    return HttpResponse("properties index.")


def create(request):
    """

    :param request:
    :return:
    """
    models_ = apps.all_models['vmf']

    fields_ = {}
    for m in models_:
        fields_[m] = get_fields('vmf', m)
    t = TemplateResponse(request, '/properties/create.html', locals())
    t.render()

    return t


def detail(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("properties detail.")


def modify(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("properties modify.")


def delete(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("properties delete.")
