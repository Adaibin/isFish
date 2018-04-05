# -*- coding: utf-8 -*-
"""log"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg
from functions import View

bp_log = Blueprint('bp_log', __name__, template_folder='templates/')

module = '日志'


class ViewLog(View):
    """ViewLog
    """
    urls = ('/vmf/log/index',
            '/vmf/log/create',
            '/vmf/log/detail',
            '/vmf/log/modify',
            '/vmf/log/delete',
            '/vmf/log/index_get',
            '/vmf/log/create_get',
            '/vmf/log/detail_get',
            '/vmf/log/modify_get',
            '/vmf/log/delete_get',
            '/vmf/log/index_post',
            '/vmf/log/create_post',
            '/vmf/log/detail_post',
            '/vmf/log/modify_post',
            '/vmf/log/delete_post')

    form = {'/vmf/log/index_post': '',
            '/vmf/log/create_post': '',
            '/vmf/log/detail_post': '',
            '/vmf/log/modify_post': '',
            '/vmf/log/delete_post': ''}

    name = dict([(url, View.f_(url, View.types) + module) for url in urls])

    def __init__(self):
        super(ViewLog, self).__init__()

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
        u1 = lg.md5s['/vmf/log/create_post']
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


class LogView(ViewLog):
    """LogView
    """
    maps = dict([(u, getattr(ViewLog, u.split('/')[-1])) for u in ViewLog.urls])
