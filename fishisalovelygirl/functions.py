# -*- coding: utf-8 -*-
"""functions"""
import hashlib
from datetime import date


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
