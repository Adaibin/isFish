# -*- coding: utf-8 -*-
"""initial"""
from string import digits
from string import ascii_letters
from string import punctuation
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from functions import wrap_dict, func_md5
from vmf.group.model import Group
from vmf.user.model import User


class InitialCreateForm(FlaskForm):
    """Initial Create"""

    w_id = StringField('w_id',
                       [validators.required(message='w_id is require.'),
                        validators.length(max=16,
                                          message="w_id's max len is 16.")])
    password = StringField('password',
                           [validators.required(message='password is require.'),
                            validators.length(max=12,
                                              message="password's max len is 12.")])
    password_ = StringField('password_',
                            [validators.required(message='password_ is require.'),
                             validators.length(max=12,
                                               message="password_'s max len is 12.")])
    user_name = StringField('user_name',
                            [validators.required(message='user name is require.'),
                             validators.length(max=16,
                                               message="user name's max len is 16.")])
    email = StringField('email',
                        [validators.required(message='email is require.'),
                         validators.length(max=64,
                                           message="email's max len is 64.")])
    group_name = StringField('group_name',
                             [validators.required(message='group name is require.'),
                              validators.length(max=32,
                                                message="group name's max len is 32.")])
    group_tag = StringField('group_tag',
                            [validators.required(message='group tag is require.'),
                             validators.length(max=16,
                                               message="group tag's max len is 16.")])

    @staticmethod
    def validate_group_name(_, field):
        """validate group name
        """
        if current_session.query(Group). \
                filter_by(name=field.data).first():
            raise ValidationError('Group exist: (%s).' % field.data)

    @staticmethod
    def validate_email(_, field):
        """validate email
        """
        if current_session.query(User). \
                filter_by(email=field.data).first():
            raise ValidationError('Group exist: (%s).' % field.data)

    @staticmethod
    def validate_w_id(_, field):
        """validate w_id
        """
        if current_session.query(User). \
                filter_by(w_id=field.data).first():
            raise ValidationError('User exist: (%s).' % field.data)

    def validate_password(self, field):
        """validate password
        """
        if field.data != self.password_.data:
            raise ValidationError('Password does not match.')
        if len(field.data) > 12 or len(field.data) < 8:
            raise ValidationError("Password's length should in [8, 12].")

        temp = 0b111
        for c in field.data:
            if c in digits:
                temp &= 0b011
            elif c in ascii_letters:
                temp &= 0b101
            elif c in punctuation:
                temp &= 0b110
            else:
                pass
        if bin(temp).count('1') > 1:
            raise ValidationError('At least two kinds of [digits, ascii_letters, punctuation]')

    def data_parser(self):
        """
        data parser
        :return:
        """
        data = self.data
        data['password'] = func_md5(data['password'])
        data.pop('csrf_token', None)

        return wrap_dict(data)
