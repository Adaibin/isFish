# -*- coding: utf-8 -*-
"""properties"""
from flask import Blueprint
from flask_restful import Resource

from app import cache

bp_properties = Blueprint('bp_properties', __name__, template_folder='jinja2_')


@bp_properties.route('/vmf/properties/index',
                     methods=['GET'],
                     endpoint='index-get')
@cache.cached(timeout=36000)
def index(type_='properties'):
    """
    index
    :param type_:
    :return:
    """
    with open(''.join(('jinja2_/', type_, '/', 'index.html'))) as f:
        return f.read()


@bp_properties.route('/vmf/properties/create',
                     methods=['GET'],
                     endpoint='create-get')
def create():
    """
    create
    :return:
    """

    return HttpResponse("properties create.")


@bp_properties.route('/vmf/properties/detail',
                     methods=['GET'],
                     endpoint='detail-get')
def detail():
    """
    detail
    :return:
    """
    return HttpResponse("properties detail.")


@bp_properties.route('/vmf/properties/modify',
                     methods=['GET'],
                     endpoint='modify-get')
def modify():
    """
    modify
    :return:
    """
    return HttpResponse("properties modify.")


@bp_properties.route('/vmf/properties/delete',
                     methods=['GET'],
                     endpoint='delete-get')
def delete():
    """
    delete
    :return:
    """
    return HttpResponse("properties delete.")


class PropertiesRes(Resource):
    """PropertiesRes
    """

    def get(self):
        """get
        """
        pass

    def put(self):
        """put
        """
        pass

    def post(self):
        """post
        """
        pass

    def delete(self):
        """delete
        """
        pass
