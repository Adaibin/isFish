# -*- coding: utf-8 -*-
"""group"""
from flask import g
from flask import jsonify
from flask import Blueprint
from flask import render_template
from app import lg
from functions import View

bp_group = Blueprint('bp_group', __name__, template_folder='templates/')

module = '组'


class ViewGroup(View):
    """ViewGroup
    """
    urls = ('/vmf/group/index',
            '/vmf/group/create',
            '/vmf/group/detail',
            '/vmf/group/modify',
            '/vmf/group/delete',
            '/vmf/group/index_get',
            '/vmf/group/create_get',
            '/vmf/group/detail_get',
            '/vmf/group/modify_get',
            '/vmf/group/delete_get',
            '/vmf/group/index_post',
            '/vmf/group/create_post',
            '/vmf/group/detail_post',
            '/vmf/group/modify_post',
            '/vmf/group/delete_post')

    form = {'/vmf/group/index_post': '',
            '/vmf/group/create_post': '',
            '/vmf/group/detail_post': '',
            '/vmf/group/modify_post': '',
            '/vmf/group/delete_post': ''}

    name = dict([(url, View.f_(url, View.types) + module) for url in urls])

    def __init__(self):
        super(ViewGroup, self).__init__()

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
        u1 = lg.md5s['/vmf/group/create_post']
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


class GroupView(ViewGroup):
    """GroupView
    """
    maps = dict([(u, getattr(ViewGroup, u.split('/')[-1])) for u in ViewGroup.urls])
