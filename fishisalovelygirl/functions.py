# -*- coding: utf-8 -*-
"""functions"""
import hashlib
from datetime import date

from flask import g
from flask import render_template
from flask_sqlalchemy_session import current_session

from vmf.log.model import Log
from app import lg


def func_md5(s, append=str(date.today()), pre=''):
    """
    func md5
    :param s: u1
    :param append: append
    :param pre: pre
    :return: md5
    """
    return hashlib.md5(''.join((pre, s, append)).encode()).hexdigest()


def get_md5s(list_):
    """
    get md5s
    :param list_:[u1, u2]
    :return: {u1: m1, u2: m2}, {m1: u1, m2: u2}
    """
    _md5s = dict([(l, func_md5(l)) for l in list_])
    _urls = dict([(_md5s[m], m) for m in _md5s])
    return _md5s, _urls


def wrap_dict(dict_):
    """
    wrap dict
    :param dict_:
    """
    return dict([(k, dict_[k].strip())for k in dict_])


class View(object):
    """View
    """
    types = {'index': '索引', 'create': '创建', 'detail': '详情',
             'modify': '修改', 'delete': '删除'}

    def __init__(self):
        self._dict = {}

    @staticmethod
    def f_(u, types_):
        for k in types_:
            if k in u:
                return types_[k]
        raise ValueError('No match type in: %s' % u)

    def get(self, url):
        """get
        """
        f = self.maps[url]
        return f(url)

    @staticmethod
    def index(url):
        """index
        """
        _get = lg.md5s['_'.join((url, 'get'))]
        return render_template(''.join((url, '.html')), **locals())

    @staticmethod
    def create(url):
        """index
        """
        return View.index(url)

    @staticmethod
    def detail(url):
        """detail
        """
        return View.index(url)

    @staticmethod
    def modify(url):
        """modify
        """
        return View.index(url)

    @staticmethod
    def delete(url):
        """delete
        """
        return View.index(url)

    @staticmethod
    def update_log(results):
        """
        update log
        :param results:
        """
        current_session.query(Log).\
            filter_by(id=g.log_id).\
            update({'results': results})
