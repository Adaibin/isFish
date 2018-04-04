# -*- coding: utf-8 -*-
"""组管理模块表验证"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from vmf.m6.model import M6
from vmf.base_form import IdVersionForm
from vmf.base_form import IdsVersionsForm


index_dict = {'name': M6.name.contains}


class M6BaseForm(FlaskForm):
    """M6 Base"""
    name = StringField('name',
                       [validators.required(message='name is require.'),
                        validators.length(max=20,
                                          message="name's max len is 20.")])
    permissions = StringField('permissions',
                              [validators.optional()])

    @staticmethod
    def validate_permissions(_, field):
        """
        validate permissions
        :param _:
        :param field:
        """
        pass

    def data_parser(self):
        """data parser"""
        data = self.data
        data.pop('csrf_token', None)
        return data


class M6IndexForm(FlaskForm):
    """M6Index"""
    NAME = '搜索组'

    endpoints = {'success': '',
                 'failed': 'bp_m6.index'}

    @staticmethod
    def validate_field(_, field):
        """
        validate field
        :param _:
        :param field:
        """
        if field.data not in index_dict:
            raise ValidationError("field's value is wrong.")

    def index_objects(self):
        """index objects"""
        value = self.value.data.strip()

        if not value:
            query = current_session.query(M6)
        else:
            cp = index_dict[self.field.data](value)
            query = current_session.query(M6).filter(cp)

        rows = query.all()
        return rows


class M6CreateForm(M6BaseForm):
    """M6 Create"""
    NAME = '添加组'

    endpoints = {'success': 'bp_m6.index',
                 'failed': ''}

    @staticmethod
    def validate_name(_, field):
        """
        validate name
        :param _:
        :param field:
        """
        if current_session.query(M6).filter_by(name=field.data).first():
            raise ValidationError('name is existed: (%s).' % field.data)


class M6ModifyForm(M6BaseForm, IdVersionForm):
    """M6 Modify"""
    NAME = '编辑组'

    target = M6
    endpoints = {'success': 'bp_m6.index',
                 'failed': ''}

    @staticmethod
    def validate_name(form, field):

        """
        validate_name
        :param form:
        :param field:
        """
        row = current_session.query(M6).\
            filter_by(**{'name': field.data}).first()
        if row and row.id != form.id.data:
            raise ValidationError('name is existed: (%s).' % field.data)


class M6DeleteForm(IdsVersionsForm):
    """M6 Delete"""
    NAME = '删除组'

    target = M6
    endpoints = {'success': 'bp_m6.index',
                 'failed': 'bp_m6.index'}

