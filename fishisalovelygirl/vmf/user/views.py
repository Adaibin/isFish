# -*- coding: utf-8 -*-
"""user"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg

bp_user = Blueprint('bp_user', __name__, template_folder='templates/')


class ViewUser(object):
    """ViewUser
    """

    def __init__(self):
        self._dict = {'/vmf/user/index': self.index,
                      '/vmf/user/create': self.index,
                      '/vmf/user/detail': self.index,
                      '/vmf/user/modify': self.index,
                      '/vmf/user/delete': self.index,
                      '/vmf/user/index-get': self.index_get,
                      '/vmf/user/create-get': self.create_get,
                      '/vmf/user/detail-get': self.detail_get,
                      '/vmf/user/modify-get': self.modify_get,
                      '/vmf/user/delete-get': self.delete_get,
                      '/vmf/user/index-post': self.index_post,
                      '/vmf/user/create-post': self.create_post,
                      '/vmf/user/detail-post': self.detail_post,
                      '/vmf/user/modify-post': self.modify_post,
                      '/vmf/user/delete-post': self.delete_post
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
        u1 = lg.md5s['/vmf/user/create']
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get(*args):
        """create
        """
        u1 = lg.md5s['/vmf/user/create-post']
        u2 = lg.md5s['/vmf/user/index']

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
