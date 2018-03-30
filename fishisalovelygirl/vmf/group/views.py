# -*- coding: utf-8 -*-
"""group"""
import json

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import session as f_session
from flask_restful import Resource


bp_group = Blueprint('bp_group', __name__, template_folder='jinja2_')


@bp_group.route('/group/index',
                methods=['GET'],
                endpoint='index-get')
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


class GroupRes(Resource):
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