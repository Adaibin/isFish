# -*- coding: utf-8 -*-
"""user"""
from flask import g
from flask import jsonify
from flask import Blueprint
from app import lg
from functions import View

bp_user = Blueprint('bp_user', __name__, template_folder='templates/')


@bp_user.route('/vmf/user/detail/<int:id_>',
               methods=['GET'], endpoint='detail')
def detail(id_):
    pass


class ViewUser(View):
    """ViewUser
    """

    def __init__(self):
        super(ViewUser, self).__init__()

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
