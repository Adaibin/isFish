# -*- coding: utf-8 -*-
"""app
"""
from flask import Flask
from werkzeug.datastructures import ImmutableDict
from flask_wtf.csrf import CSRFProtect
from flask.ext.cache import Cache


SECRET_KEY = 'V4zdc5UTM6eWa8C2qgYRt0su7oiFwSrN'


def create_app():
    """create app
    """
    app_ = Flask(__name__)

    app_.debug = True
    app_.secret_key = SECRET_KEY
    #
    app_.permanent_session_lifetime = 144000

    app_.jinja_options = ImmutableDict(extensions=['jinja2.ext.autoescape',
                                                   'jinja2.ext.with_',
                                                   'jinja2.ext.do',
                                                   'jinja2.ext.loopcontrols'])
    app_.config.update(**{'WTF_CSRF_SECRET_KEY': SECRET_KEY,
                          'WTF_CSRF_TIME_LIMIT': 14400})
    csrf = CSRFProtect()
    csrf.init_app(app_)
    app_.__setattr__('csrf', csrf)

    return app_


lg = create_app()
cache = None
# cache = Cache(lg, config={'CACHE_TYPE': 'redis',
#                           'host': '127.0.0.1',
#                           'port': '6379'})
