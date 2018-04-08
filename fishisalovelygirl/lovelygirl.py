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
from flask.ext.login import logout_user
from flask_login import login_required
from flask_sqlalchemy_session import current_session
from flask_sqlalchemy_session import flask_scoped_session

from app import lg
from blueprints import register_bp
from vmf.properties.views import PropertiesView
from vmf.user.model import User
from vmf.user.views import UserView
from vmf.group.views import GroupView
from vmf.log.views import LogView
from vmf.log.model import Log
from functions import get_md5s
from mysql_engine import session_factory
from app import login_manager

urls = GroupView.urls \
       + UserView.urls \
       + PropertiesView.urls \
       + LogView.urls

register_bp(lg)

flask_session = flask_scoped_session(session_factory, lg)

views = {'properties': PropertiesView,
         'user': UserView,
         'group': GroupView,
         'log': LogView}


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


@login_manager.unauthorized_handler
def unauthorized():
    """unauthorized
    """
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    """load user
    """
    return current_session.query(User).\
        filter_by(id=user_id).first()


@lg.route("/sign_out")
@login_required
def sign_out():
    """sign out
    """
    logout_user()
    return redirect('/')


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
    view = views[url.split('/')[2]]

    if request.method == 'POST' and view.form[url]:
        # create log
        log_data = {'user_id': fs['user_id'],
                    'time_': datetime.now(),
                    'form': json.dumps(g.form.data)}
        log = Log(**log_data)
        current_session.add(log)
        current_session.refresh()
        current_session.commit()

        g.log_id = log.id
        g.form = view.form[url]()

        if not g.form.validate():
            message = ' '.join([', '.join(er) for er in g.form.errors.values()])
            results = {'status': False, 'message': message}
            # update log
            current_session.query(Log).\
                filter_by(id=g.log_id).\
                update({'results': results})
            return jsonify(results)

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
                             ]})


if __name__ == '__main__':
    lg.run(host='192.168.4.214', port=9755, threaded=True)
