# -*- coding: utf-8 -*-
"""user"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from functions import wrap_dict, func_md5
from vmf.user.model import User


class SignInForm(FlaskForm):
    """Sign In"""

    w_id = StringField('w_id',
                       [validators.required(message='w_id is require.'),
                        validators.length(max=16,
                                          message="w_id's max len is 16.")])
    password = StringField('password',
                           [validators.required(message='password is require.'),
                            validators.length(max=12,
                                              message="password's max len is 12.")])

    def validate_password(self, field):
        """validate password
        """
        user = current_session.query(User).\
            filter_by(w_id=self.w_id.data).first()
        if not user:
            raise ValidationError('workspace id or password is wrong.')
        if user.password != func_md5(field.data):
            raise ValidationError('workspace id or password is wrong.')

    def data_parser(self):
        """
        data parser
        :return:
        """
        data = self.data
        data.pop('csrf_token', None)

        return wrap_dict(data)
