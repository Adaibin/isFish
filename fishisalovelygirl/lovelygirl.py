# -*- coding: utf-8 -*-
"""lg"""
import json
from datetime import date
from datetime import datetime

from flask import g
from flask import jsonify
from flask import request
from flask import redirect
from flask import session as fs
from flask_login import login_required
from flask_sqlalchemy_session import current_session
from flask_sqlalchemy_session import flask_scoped_session

from app import lg
from blueprints import register_bp
from blueprints import urls
from vmf.properties.views import ViewProperties
from vmf.user.views import ViewUser
from vmf.group.views import ViewGroup
from vmf.log.views import ViewLog
from vmf.m2.views import ViewM2
from vmf.m3.views import ViewM3
from vmf.m4.views import ViewM4
from vmf.m5.views import ViewM5
from vmf.m6.views import ViewM6
from vmf.m7.views import ViewM7
from vmf.m8.views import ViewM8
from vmf.m9.views import ViewM9
from vmf.log.model import Log
from functions import get_md5s
from mysql_engine import session_factory


register_bp(lg)
flask_session = flask_scoped_session(session_factory, lg)

views = {'properties': ViewProperties,
         'user': ViewUser,
         'group': ViewGroup,
         'log': ViewLog,
         'm2': ViewM2,
         'm3': ViewM3,
         'm4': ViewM4,
         'm5': ViewM5,
         'm6': ViewM6,
         'm7': ViewM7,
         'm8': ViewM8,
         'm9': ViewM9}


@lg.before_request
def before():
    """before
    """
    # update md5s & urls
    md5_time = getattr(lg, 'md5_time', None)
    if str(date.today()) != md5_time:
        lg.urls_pre = getattr(lg, 'urls', None)
        lg.md5s, lg.urls = get_md5s(urls)
        lg.md5_time = str(date.today())


@lg.after_request
def after(response):
    """after
    """
    return response


@lg.route('/vmf/md5/<string:md5>',
          methods=['GET', 'POST'], endpoint='md5')
@login_required
def visit_md5(md5):
    """
    visit by md5
    :param md5:
    :return:
    """
    if md5 not in lg.urls and md5 not in lg.urls_pre:
        return redirect('/')

    url = lg.urls[md5] if md5 in lg.urls else lg.urls_pre[md5]

    if request.method == 'POST' and urls[url]:
        # create log
        log_data = {'user_id': fs['user_id'],
                    'time_': datetime.now(),
                    'form': json.dumps(g.form.data)}
        log = Log(**log_data)
        current_session.add(log)
        current_session.refresh()
        current_session.commit()

        g.log_id = log.id
        g.form = urls[url]()

        if not g.form.validate():
            message = ' '.join([', '.join(er) for er in g.form.errors.values()])
            results = {'status': False, 'message': message}
            # update log
            current_session.query(Log).\
                filter_by(id=g.log_id).\
                update({'results': results})
            return jsonify(results)

    view = views[url.split('/')[2]]
    return view().get(url)


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
                             md5s['/vmf/properties/index'],

                             md5s['/vmf/log/index'],
                             md5s['/vmf/m2/index'],

                             md5s['/vmf/m3/index'],
                             md5s['/vmf/m4/index'],
                             md5s['/vmf/m5/index'],

                             md5s['/vmf/m6/index'],
                             md5s['/vmf/m7/index'],
                             md5s['/vmf/m8/index'],

                             md5s['/vmf/m9/index'],
                             ]})


if __name__ == '__main__':
    lg.run(host='192.168.4.214', port=9755, threaded=True)
