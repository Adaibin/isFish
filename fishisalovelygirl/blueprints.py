# -*- coding: utf-8 -*-
"""blue print
"""
from flask_restful import Api

from vmf.properties.views import bp_properties
from vmf.properties.views import PropertiesRes
from vmf.group.views import bp_group
from vmf.group.views import GroupRes
from vmf.user.views import bp_user
from vmf.user.views import UserRes


def register_bp(app_):
    """register bp
    """
    #
    app_.register_blueprint(bp_properties)
    #
    app_.register_blueprint(bp_group)
    #
    app_.register_blueprint(bp_user)

    api = Api(app_)
    api.add_resource(PropertiesRes, '/rest/properties/<int:id_>')
    api.add_resource(GroupRes, '/rest/group/<int:id_>')
    api.add_resource(UserRes, '/rest/user/<int:id_>')
    # api.add_resource(UserRes, '/rest/md5/<string:md5>')



