# -*- coding: utf-8 -*-
"""user"""
from flask import g
from flask import jsonify
from flask import Blueprint
from app import lg
from functions import View

bp_user = Blueprint('bp_user', __name__, template_folder='templates/')
module = '用户'


@bp_user.route('/vmf/user/detail/<int:id_>',
               methods=['GET'], endpoint='detail')
def detail(id_):
    pass


class ViewUser(View):
    """ViewUser
    """
    urls = ('/vmf/user/index',
            '/vmf/user/create',
            '/vmf/user/detail',
            '/vmf/user/modify',
            '/vmf/user/delete',
            '/vmf/user/index_get',
            '/vmf/user/create_get',
            '/vmf/user/detail_get',
            '/vmf/user/modify_get',
            '/vmf/user/delete_get',
            '/vmf/user/index_post',
            '/vmf/user/create_post',
            '/vmf/user/detail_post',
            '/vmf/user/modify_post',
            '/vmf/user/delete_post')

    form = {'/vmf/user/index_post': '',
            '/vmf/user/create_post': '',
            '/vmf/user/detail_post': '',
            '/vmf/user/modify_post': '',
            '/vmf/user/delete_post': ''}

    name = dict([(url, View.f_(url, View.types) + module) for url in urls])

    def __init__(self):
        super(ViewUser, self).__init__()

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
        u1 = lg.md5s['/vmf/user/create_post']
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
    def create_post(self, *args):
        """create
        """
        form = g.form
        results = {'status': True, 'message': 'Create success!'}
        super().update_log(results)
        return jsonify(results)

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


class UserView(ViewUser):
    """UserView
    """
    maps = dict([(u, getattr(ViewUser, u.split('/')[-1])) for u in ViewUser.urls])
