# -*- coding: utf-8 -*-
"""app
"""
from flask import Flask


def create_app():
    """create app
    """
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'V4zdc5UTM6eWaxC1qgYRs0su7oiFwSrN'

    return app


app_ = create_app()
