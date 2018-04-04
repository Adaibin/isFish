# -*- coding: utf-8 -*-
"""lg"""
import hashlib
from datetime import date

from flask import jsonify

from app import lg
from blueprints import register_bp
from blueprints import urls
from vmf.properties.views import ViewProperties
from vmf.user.views import ViewUser
from vmf.group.views import ViewGroup

register_bp(lg)

views = {'properties': ViewProperties,
         'user': ViewUser,
         'group': ViewGroup}


@lg.before_request
def before():
    """before
    """
    # update md5s & urls
    md5_time = getattr(lg, 'md5_time', None)
    if str(date.today()) != md5_time:
        lg.md5s, lg.urls = get_md5s(urls)
        lg.md5_time = str(date.today())


@lg.route('/vmf/md5/<string:md5>',
          methods=['GET', 'POST'],
          endpoint='md5')
def visit_md5(md5):
    """
    visit by md5
    :param md5:
    :return:
    """
    url = lg.urls[md5]
    view = views[url.split('/')[2]]
    return view().get(url)


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


@lg.route('/', methods=['GET'], endpoint='YLP')
def ylp():
    """
    ylp
    """
    with open('templates/ylp.html', encoding='utf-8') as f:
        return f.read()


@lg.route('/-get', methods=['GET'], endpoint='YLP-get')
def ylp_get():
    """
    ylp
    """
    md5s = lg.md5s
    return jsonify({'urls': [md5s['/vmf/user/index'],
                             md5s['/vmf/group/index'],
                             md5s['/vmf/properties/index'], ]})


if __name__ == '__main__':
    lg.run(host='192.168.4.214', port=9755)
