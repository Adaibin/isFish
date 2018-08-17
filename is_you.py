# -*- coding: utf-8 -*-
"""run_"""

from flask import render_template

from app import app_


@app_.before_request
def before():
    """before
    """
    pass


@app_.route("/", methods=['GET'], endpoint='index')
def index():
    """index
    """
    return render_template('/index.html')


@app_.before_first_request
def first_request():
    pass


if __name__ == '__main__':
    app_.run(host='0.0.0.0', port=80, use_reloader=True)
