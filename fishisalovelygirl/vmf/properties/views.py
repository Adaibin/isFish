# -*- coding: utf-8 -*-
"""properties"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg

from vmf.group.model import Group
from vmf.user.model import User
from vmf.properties.model import Properties

bp_properties = Blueprint('bp_properties', __name__, template_folder='templates/')


class ViewProperties(object):
    """ViewProperties
    """

    def __init__(self):
        self._dict = {'/vmf/properties/index': self.index,
                      '/vmf/properties/create': self.index,
                      '/vmf/properties/detail': self.index,
                      '/vmf/properties/modify': self.index,
                      '/vmf/properties/delete': self.index,
                      '/vmf/properties/index-get': self.index_get,
                      '/vmf/properties/create-get': self.create_get,
                      '/vmf/properties/detail-get': self.detail_get,
                      '/vmf/properties/modify-get': self.modify_get,
                      '/vmf/properties/delete-get': self.delete_get,
                      '/vmf/properties/index-post': self.index_post,
                      '/vmf/properties/create-post': self.create_post,
                      '/vmf/properties/detail-post': self.detail_post,
                      '/vmf/properties/modify-post': self.modify_post,
                      '/vmf/properties/delete-post': self.delete_post
                      }

    def get(self, url):
        """get
        """
        return self._dict[url](url)

    @staticmethod
    def index(url):
        """index
        """
        _get = lg.md5s['-'.join((url, 'get'))]
        return render_template(''.join((url, '.html')), **locals())

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

        u1 = lg.md5s['/vmf/properties/create-post']
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
