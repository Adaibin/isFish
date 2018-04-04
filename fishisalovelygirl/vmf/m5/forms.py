# -*- coding: utf-8 -*-
"""组管理模块表验证"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from vmf.m5.model import M5
from vmf.base_form import IdVersionForm
from vmf.base_form import IdsVersionsForm


index_dict = {'name': M5.name.contains}


class M5BaseForm(FlaskForm):
    """M5 Base"""
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


class M5IndexForm(FlaskForm):
    """M5Index"""
    NAME = '搜索组'

    endpoints = {'success': '',
                 'failed': 'bp_m5.index'}

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
            query = current_session.query(M5)
        else:
            cp = index_dict[self.field.data](value)
            query = current_session.query(M5).filter(cp)

        rows = query.all()
        return rows


class M5CreateForm(M5BaseForm):
    """M5 Create"""
    NAME = '添加组'

    endpoints = {'success': 'bp_m5.index',
                 'failed': ''}

    @staticmethod
    def validate_name(_, field):
        """
        validate name
        :param _:
        :param field:
        """
        if current_session.query(M5).filter_by(name=field.data).first():
            raise ValidationError('name is existed: (%s).' % field.data)


class M5ModifyForm(M5BaseForm, IdVersionForm):
    """M5 Modify"""
    NAME = '编辑组'

    target = M5
    endpoints = {'success': 'bp_m5.index',
                 'failed': ''}

    @staticmethod
    def validate_name(form, field):

        """
        validate_name
        :param form:
        :param field:
        """
        row = current_session.query(M5).\
            filter_by(**{'name': field.data}).first()
        if row and row.id != form.id.data:
            raise ValidationError('name is existed: (%s).' % field.data)


class M5DeleteForm(IdsVersionsForm):
    """M5 Delete"""
    NAME = '删除组'

    target = M5
    endpoints = {'success': 'bp_m5.index',
                 'failed': 'bp_m5.index'}
