# -*- coding: utf-8 -*-
"""log"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg

bp_log = Blueprint('bp_log', __name__, template_folder='templates/')


class ViewLog(object):
    """ViewLog
    """

    def __init__(self):
        self._dict = {'/vmf/log/index': self.index,
                      '/vmf/log/create': self.index,
                      '/vmf/log/detail': self.index,
                      '/vmf/log/modify': self.index,
                      '/vmf/log/delete': self.index,
                      '/vmf/log/index-get': self.index_get,
                      '/vmf/log/create-get': self.create_get,
                      '/vmf/log/detail-get': self.detail_get,
                      '/vmf/log/modify-get': self.modify_get,
                      '/vmf/log/delete-get': self.delete_get,
                      '/vmf/log/index-post': self.index_post,
                      '/vmf/log/create-post': self.create_post,
                      '/vmf/log/detail-post': self.detail_post,
                      '/vmf/log/modify-post': self.modify_post,
                      '/vmf/log/delete-post': self.delete_post
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
        u1 = lg.md5s['/vmf/log/create']
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get(*args):
        """create
        """
        u1 = lg.md5s['/vmf/log/create-post']
        u2 = lg.md5s['/vmf/log/index']
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
