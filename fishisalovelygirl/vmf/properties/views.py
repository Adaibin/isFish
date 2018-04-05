# -*- coding: utf-8 -*-
"""properties"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg
from functions import View

from vmf.group.model import Group
from vmf.user.model import User
from vmf.properties.model import Properties

bp_properties = Blueprint('bp_properties', __name__, template_folder='templates/')
module = '属性'


class ViewProperties(View):
    """ViewProperties
    """
    urls = ('/vmf/properties/index',
            '/vmf/properties/create',
            '/vmf/properties/detail',
            '/vmf/properties/modify',
            '/vmf/properties/delete',
            '/vmf/properties/index_get',
            '/vmf/properties/create_get',
            '/vmf/properties/detail_get',
            '/vmf/properties/modify_get',
            '/vmf/properties/delete_get',
            '/vmf/properties/index_post',
            '/vmf/properties/create_post',
            '/vmf/properties/detail_post',
            '/vmf/properties/modify_post',
            '/vmf/properties/delete_post')

    form = {'/vmf/properties/index_post': '',
            '/vmf/properties/create_post': '',
            '/vmf/properties/detail_post': '',
            '/vmf/properties/modify_post': '',
            '/vmf/properties/delete_post': ''}

    name = dict([(url, View.f_(url, View.types) + module) for url in urls])

    def __init__(self):
        super(ViewProperties, self).__init__()

    @staticmethod
    def index_get(*args):
        """index
        """
        u1 = lg.md5s['/vmf/properties/create']
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get(*args):
        """create
        """

        def func_(table):
            """
            get table's columns
            :param table:
            :return:
            """
            return table.__table__.columns._data._list

        u1 = lg.md5s['/vmf/properties/create_post']
        u2 = lg.md5s['/vmf/properties/index']

        return jsonify({'tables': sorted(['User', 'Properties', 'Properties']),
                        'fields': {'User': func_(User),
                                   'Group': func_(Group),
                                   'Properties': func_(Properties)},
                        'urls': [u1, u2]})

    @staticmethod
    def detail_get(*args):
        """detail
        """
        pass

    @staticmethod
    def modify_get(*args):
        """modify
        """
        pass

    @staticmethod
    def delete_get(*args):
        """delete
        """
        pass

    @staticmethod
    def index_post(*args):
        """index
        """
        pass

    @staticmethod
    def create_post(*args):
        """create
        """
        form = g.form
        return jsonify({'status': True, 'message': 'Create success!'})

    @staticmethod
    def detail_post(*args):
        """detail
        """
        pass

    @staticmethod
    def modify_post(*args):
        """modify
        """
        pass

    @staticmethod
    def delete_post(*args):
        """delete
        """
        pass


class PropertiesView(ViewProperties):
    """ViewProperties_
    """
    maps = dict([(u, getattr(ViewProperties, u.split('/')[-1])) for u in ViewProperties.urls])
