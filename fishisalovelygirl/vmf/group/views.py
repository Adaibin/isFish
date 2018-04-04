# -*- coding: utf-8 -*-
"""group"""
from flask import jsonify
from flask import Blueprint
from flask import render_template
from vmf.user.model import User
from vmf.group.model import Group
from vmf.properties.model import Properties
from app import lg

bp_group = Blueprint('bp_group', __name__, template_folder='templates/')


class ViewGroup(object):
    """ViewGroup
    """

    def __init__(self):
        self._dict = {'/vmf/group/index': self.index,
                      '/vmf/group/create': self.index,
                      '/vmf/group/detail': self.index,
                      '/vmf/group/modify': self.index,
                      '/vmf/group/delete': self.index,
                      '/vmf/group/index-get': self.index_get,
                      '/vmf/group/create-get': self.create_get,
                      '/vmf/group/detail-get': self.detail_get,
                      '/vmf/group/modify-get': self.modify_get,
                      '/vmf/group/delete-get': self.delete_get
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
        u1 = lg.md5s['/vmf/group/create']
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

        u1 = lg.md5s['/vmf/group/index']

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
