# -*- coding: utf-8 -*-
"""properties"""
from flask import jsonify
from flask import Blueprint
from flask import request
from flask import render_template
from flask_restful import Resource
from sqlalchemy.orm.attributes import InstrumentedAttribute

from functions import url_to_md5
from vmf.user.model import User
from vmf.group.model import Group
from vmf.properties.model import Properties
from app import cache

bp_properties = Blueprint('bp_properties', __name__, template_folder='templates/')

pre_path = '/properties/'


@bp_properties.route('/vmf/properties/index',
                     methods=['GET'],
                     endpoint='index')
@bp_properties.route('/vmf/properties/detail',
                     methods=['GET'],
                     endpoint='detail')
@bp_properties.route('/vmf/properties/create',
                     methods=['GET'],
                     endpoint='create')
@bp_properties.route('/vmf/properties/modify',
                     methods=['GET'],
                     endpoint='modify')
@bp_properties.route('/vmf/properties/delete',
                     methods=['GET'],
                     endpoint='delete')
# @cache.cached(timeout=36000)
def index():
    """
    index
    :return:
    """
    if '.' in request.endpoint:
        endpoint = request.endpoint.split('.')[-1]
    else:
        endpoint = request.endpoint

    axios = '-'.join((request.path, 'get'))
    axios_ = url_to_md5(axios)

    return render_template(''.join((pre_path, endpoint, '.html')),
                           **locals())
    # with open(''.join((pre_path, endpoint, '.html'))) as f:
    #     html = f.read()
    #     html.format(axios=axios_)
    #     return html


@bp_properties.route('/vmf/properties/index-get', methods=['GET'],
                     endpoint='index-get')
def index_():
    """index_
    """

    u1 = url_to_md5('/vmf/properties/create')

    return jsonify({'urls': [u1, ]})


@bp_properties.route('/vmf/properties/create-get', methods=['GET'],
                     endpoint='create-get')
def create_():
    """create_
    """

    def func_(table):
        """
        get table's columns
        :param table:
        :return:
        """
        return table.__table__.columns._data._list

    u1 = url_to_md5('/vmf/properties/index')

    return jsonify({'tables': sorted(['User', 'Group', 'Properties']),
                    'fields': {'User': func_(User),
                               'Group': func_(Group),
                               'Properties': func_(Properties)},
                    'urls': [u1, ]
                    })


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
