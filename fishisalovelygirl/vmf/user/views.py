# -*- coding: utf-8 -*-
"""user"""
import json

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import session as f_session

from flask_restful import Resource


bp_user = Blueprint('bp_user', __name__, template_folder='jinja2_')


@bp_user.route('/user/index',
               methods=['GET'],
               endpoint='index-get')
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


class UserRes(Resource):
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
