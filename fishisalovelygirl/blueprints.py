# -*- coding: utf-8 -*-
"""blue print
"""
from vmf.properties.views import bp_properties
from vmf.group.views import bp_group
from vmf.user.views import bp_user
from vmf.initial.views import bp_initial


def register_bp(app_):
    """register bp
    """
    app_.register_blueprint(bp_properties)
    #
    app_.register_blueprint(bp_group)
    #
    app_.register_blueprint(bp_user)
    app_.register_blueprint(bp_initial)
