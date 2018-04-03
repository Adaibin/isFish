# -*- coding: utf-8 -*-
"""lg"""
import hashlib
from datetime import datetime

from flask import g
from flask import jsonify
from flask import redirect
from flask import request
from flask import current_app
from flask import make_response
from flask import session as fs
import requests

from app import lg, cache
from blueprints import register_bp
from blueprints import urls


register_bp(lg)


@lg.before_request
def before():
    """before
    """
    print('before')


@lg.after_request
def after(response):
    """after
    """
    print('after')
    return response


@lg.route('/vmf/md5/<string:md5>',
          methods=['GET', 'POST'],
          endpoint='md5')
def md5_to_url(md5):
    """translate md5 to url
    """
    _, _urls = url_md5(urls)
    url = _urls[md5]
    return url


def func_md5(url):
    """func_md5
    """
    return hashlib.md5(''.join((url, str(datetime.today()))).encode()).hexdigest()


@cache.cached(timeout=60 * 60, key_prefix='url_md5')
def url_md5(urls_):
    """
    : paras urls_:
    """
    _md5s = dict([(url, func_md5(url)) for url in urls_])
    _urls = dict([(_md5s[url], url) for url in _md5s])
    return _md5s, _urls


@lg.route('/', methods=['GET'], endpoint='YLP')
def ylp():
    """
    ylp
    """
    _md5s, _urls = url_md5(urls)
    return


@lg.route('/-get', methods=['GET'], endpoint='YLP-get')
def ylp():
    """
    ylp
    """
    _md5s, _ = url_md5(urls)
    return jsonify({'urls': [_md5s['/vmf/user/index'],
                             _md5s['/vmf/group/index'],
                             _md5s['/vmf/properties/index'], ]})


if __name__ == '__main__':
    lg.run(host='192.168.4.214', port=9755)
