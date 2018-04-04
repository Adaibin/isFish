# -*- coding: utf-8 -*-
"""组管理模块表验证"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from vmf.m2.model import M2
from vmf.base_form import IdVersionForm
from vmf.base_form import IdsVersionsForm


index_dict = {'name': M2.name.contains}


class M2BaseForm(FlaskForm):
    """M2 Base"""
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


class M2IndexForm(FlaskForm):
    """M2Index"""
    NAME = '搜索组'

    endpoints = {'success': '',
                 'failed': 'bp_m2.index'}

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
            query = current_session.query(M2)
        else:
            cp = index_dict[self.field.data](value)
            query = current_session.query(M2).filter(cp)

        rows = query.all()
        return rows


class M2CreateForm(M2BaseForm):
    """M2 Create"""
    NAME = '添加组'

    endpoints = {'success': 'bp_m2.index',
                 'failed': ''}

    @staticmethod
    def validate_name(_, field):
        """
        validate name
        :param _:
        :param field:
        """
        if current_session.query(M2).filter_by(name=field.data).first():
            raise ValidationError('name is existed: (%s).' % field.data)


class M2ModifyForm(M2BaseForm, IdVersionForm):
    """M2 Modify"""
    NAME = '编辑组'

    target = M2
    endpoints = {'success': 'bp_m2.index',
                 'failed': ''}

    @staticmethod
    def validate_name(form, field):

        """
        validate_name
        :param form:
        :param field:
        """
        row = current_session.query(M2).\
            filter_by(**{'name': field.data}).first()
        if row and row.id != form.id.data:
            raise ValidationError('name is existed: (%s).' % field.data)


class M2DeleteForm(IdsVersionsForm):
    """M2 Delete"""
    NAME = '删除组'

    target = M2
    endpoints = {'success': 'bp_m2.index',
                 'failed': 'bp_m2.index'}
