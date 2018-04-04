# -*- coding: utf-8 -*-
"""blue print
"""
from vmf.properties.views import bp_properties
from vmf.group.views import bp_group
from vmf.user.views import bp_user


def register_bp(app_):
    """register bp
    """
    #
    app_.register_blueprint(bp_properties)
    #
    app_.register_blueprint(bp_group)
    #
    app_.register_blueprint(bp_user)

    # api = Api(app_)
    # api.add_resource(PropertiesRes, '/rest/properties/<int:id_>')
    # api.add_resource(GroupRes, '/rest/group/<int:id_>')
    # api.add_resource(UserRes, '/rest/user/<int:id_>')
    # # api.add_resource(UserRes, '/rest/md5/<string:md5>')


urls = ('/vmf/properties/index',
        '/vmf/properties/create',
        '/vmf/properties/detail',
        '/vmf/properties/modify',
        '/vmf/properties/delete',
        '/vmf/properties/index-get',
        '/vmf/properties/create-get',
        '/vmf/properties/detail-get',
        '/vmf/properties/modify-get',
        '/vmf/properties/delete-get',

        '/vmf/user/index',
        '/vmf/user/create',
        '/vmf/user/detail',
        '/vmf/user/modify',
        '/vmf/user/delete',
        '/vmf/user/index-get',
        '/vmf/user/create-get',
        '/vmf/user/detail-get',
        '/vmf/user/modify-get',
        '/vmf/user/delete-get',

        '/vmf/group/index',
        '/vmf/group/create',
        '/vmf/group/detail',
        '/vmf/group/modify',
        '/vmf/group/delete',
        '/vmf/group/index-get',
        '/vmf/group/create-get',
        '/vmf/group/detail-get',
        '/vmf/group/modify-get',
        '/vmf/group/delete-get',
        )
