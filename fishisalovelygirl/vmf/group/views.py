# -*- coding: utf-8 -*-
"""group"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
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
                      '/vmf/group/delete-get': self.delete_get,
                      '/vmf/group/index-post': self.index_post,
                      '/vmf/group/create-post': self.create_post,
                      '/vmf/group/detail-post': self.detail_post,
                      '/vmf/group/modify-post': self.modify_post,
                      '/vmf/group/delete-post': self.delete_post
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
        u1 = lg.md5s['/vmf/group/create']
        return jsonify({'urls': [u1, ]})

    @staticmethod
    def create_get(*args):
        """create
        """
        u1 = lg.md5s['/vmf/group/create-post']
        u2 = lg.md5s['/vmf/group/index']
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
