# -*- coding: utf-8 -*-
"""properties"""
from flask import jsonify
from flask import Blueprint
from flask import render_template
from vmf.user.model import User
from vmf.group.model import Group
from vmf.properties.model import Properties
from app import lg

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
                      '/vmf/properties/delete-get': self.delete_get
                      }

    def get(self, url):
        """get
        """
        return self._dict[url](url)

    @staticmethod
    def index(url):
        """index
        """
        axios_ = lg.md5s['-'.join((url, 'get'))]
        return render_template(''.join((url, '.html')), **locals())

    @staticmethod
    def index_get(*args):
        """index
        """
        u1 = lg.md5s['/vmf/properties/create']
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get(*args):
        """index
        """

        def func_(table):
            """
            get table's columns
            :param table:
            :return:
            """
            return table.__table__.columns._data._list

        u1 = lg.md5s['/vmf/properties/index']

        return jsonify({'tables': sorted(['User', 'Group', 'Properties']),
                        'fields': {'User': func_(User),
                                   'Group': func_(Group),
                                   'Properties': func_(Properties)},
                        'urls': [u1, ]})

    @staticmethod
    def detail_get(*args):
        """index
        """
        pass

    @staticmethod
    def modify_get(*args):
        """index
        """
        pass

    @staticmethod
    def delete_get(*args):
        """index
        """
        pass
