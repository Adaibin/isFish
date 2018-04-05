# -*- coding: utf-8 -*-
"""initial"""
from flask import jsonify
from flask import Blueprint
from flask import render_template
from flask_sqlalchemy_session import current_session

from vmf.initial.forms import InitialCreateForm
from vmf.user.model import User
from vmf.group.model import Group

bp_initial = Blueprint('bp_initial', __name__, template_folder='templates/')


@bp_initial.route('/vmf/initial/index',
                  methods=['GET'], endpoint='index')
def index():
    admin_group = current_session.query(Group). \
        filter_by(tag='admin').first()
    valid = False
    if not admin_group:
        valid = True
        message = 'Pls create a group with "admin" tag.'
        return render_template('/vmf/initial/index.html', **locals())

    admin = current_session.query(User). \
        filter_by(group_id=admin_group.id).first()
    if not admin:
        valid = True
        message = 'Pls create a user in a group which with "admin" tag.'
        return render_template('/vmf/initial/index.html', **locals())

    message = """Group&User(admin) had been created,
    This module can't be use again."""
    return render_template('/vmf/initial/index.html', **locals())


@bp_initial.route('/vmf/initial/create',
                  methods=['POST'], endpoint='create')
def create():
    form = InitialCreateForm()
    if not form.validate():
        message = ' '.join([', '.join(er) for er in form.errors.values()])
        results = {'status': False, 'message': message}
        return jsonify(results)
    data = form.data_parser()
    try:
        group = Group(**{'name': data['group_name'],
                         'tag': data['tag'],
                         'permissions': 'all'})
        current_session.add(group)
        current_session.refresh()
        current_session.commit()

        user = User(**{'name': data['user_name'],
                       'password': data['password'],
                       'w_id': data['w_id'],
                       'email': data['email'],
                       'group_id': group.id})
        current_session.add(user)
        current_session.refresh()
        current_session.commit()
        return jsonify({'status': True, 'message': 'Create success.'})
    except Exception as e:
        results = {'status': False, 'message': str(e)}
        return jsonify(results)
