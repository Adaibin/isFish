# -*- coding: utf-8 -*-
"""组管理模块表验证"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from vmf.m4.model import M4
from vmf.base_form import IdVersionForm
from vmf.base_form import IdsVersionsForm


index_dict = {'name': M4.name.contains}


class M4BaseForm(FlaskForm):
    """M4 Base"""
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


class M4IndexForm(FlaskForm):
    """M4Index"""
    NAME = '搜索组'

    endpoints = {'success': '',
                 'failed': 'bp_m4.index'}

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
            query = current_session.query(M4)
        else:
            cp = index_dict[self.field.data](value)
            query = current_session.query(M4).filter(cp)

        rows = query.all()
        return rows


class M4CreateForm(M4BaseForm):
    """M4 Create"""
    NAME = '添加组'

    endpoints = {'success': 'bp_m4.index',
                 'failed': ''}

    @staticmethod
    def validate_name(_, field):
        """
        validate name
        :param _:
        :param field:
        """
        if current_session.query(M4).filter_by(name=field.data).first():
            raise ValidationError('name is existed: (%s).' % field.data)


class M4ModifyForm(M4BaseForm, IdVersionForm):
    """M4 Modify"""
    NAME = '编辑组'

    target = M4
    endpoints = {'success': 'bp_m4.index',
                 'failed': ''}

    @staticmethod
    def validate_name(form, field):

        """
        validate_name
        :param form:
        :param field:
        """
        row = current_session.query(M4).\
            filter_by(**{'name': field.data}).first()
        if row and row.id != form.id.data:
            raise ValidationError('name is existed: (%s).' % field.data)


class M4DeleteForm(IdsVersionsForm):
    """M4 Delete"""
    NAME = '删除组'

    target = M4
    endpoints = {'success': 'bp_m4.index',
                 'failed': 'bp_m4.index'}

