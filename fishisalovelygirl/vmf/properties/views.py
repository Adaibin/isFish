# -*- coding: utf-8 -*-
"""properties"""
from flask import jsonify
from flask import jsonify
from flask import Blueprint
from flask import request
from flask import redirect
from flask import render_template
from flask import make_response
from flask import session as fs
from flask_restful import Resource

from functions import url_to_md5
from vmf.user.model import User
from vmf.group.model import Group
from vmf.properties.model import Properties
from app import cache

bp_properties = Blueprint('bp_properties', __name__, template_folder='templates/')


class RequestMd5(object):
    """RequestMd5
    """

    def __init__(self):
        self._dict = {'/vmf/properties/index': self.index,
                      '/vmf/properties/create': self.index,
                      '/vmf/properties/detail': self.index,
                      '/vmf/properties/modify': self.index,
                      '/vmf/properties/delete': self.index}

    def get(self, url):
        """get
        """
        self._dict[url](url)

    @staticmethod
    def index(url):
        """index
        """
        axios_ = url_to_md5('-'.join((url, 'get')))
        return render_template(''.join((url, '.html')), **locals())

    @staticmethod
    def index_get():
        """index
        """
        u1 = url_to_md5('/vmf/properties/create')
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get():
        """index
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
                        'urls': [u1, ]})

    @staticmethod
    def detail_get():
        """index
        """
        pass

    @staticmethod
    def modify_get():
        """index
        """
        pass

    @staticmethod
    def delete_get():
        """index
        """
        pass


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
