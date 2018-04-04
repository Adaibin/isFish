# -*- coding: utf-8 -*-
"""m1"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg

bp_m1 = Blueprint('bp_m1', __name__, template_folder='templates/')


class ViewM1(object):
    """ViewM1
    """

    def __init__(self):
        self._dict = {'/vmf/m1/index': self.index,
                      '/vmf/m1/create': self.index,
                      '/vmf/m1/detail': self.index,
                      '/vmf/m1/modify': self.index,
                      '/vmf/m1/delete': self.index,
                      '/vmf/m1/index-get': self.index_get,
                      '/vmf/m1/create-get': self.create_get,
                      '/vmf/m1/detail-get': self.detail_get,
                      '/vmf/m1/modify-get': self.modify_get,
                      '/vmf/m1/delete-get': self.delete_get,
                      '/vmf/m1/index-post': self.index_post,
                      '/vmf/m1/create-post': self.create_post,
                      '/vmf/m1/detail-post': self.detail_post,
                      '/vmf/m1/modify-post': self.modify_post,
                      '/vmf/m1/delete-post': self.delete_post
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
        u1 = lg.md5s['/vmf/m1/create']
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get(*args):
        """create
        """
        u1 = lg.md5s['/vmf/m1/create-post']
        u2 = lg.md5s['/vmf/m1/index']
        return jsonify({'urls': [u1, u2]})

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
