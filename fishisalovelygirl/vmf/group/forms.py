# -*- coding: utf-8 -*-
"""Group
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from wtforms import validators
from flask_sqlalchemy_session import current_session

from vmf.group.model import Group
from vmf.base_form import IdVersionForm
from vmf.base_form import IdsVersionsForm


index_dict = {'name': Group.name.contains}


class GroupBaseForm(FlaskForm):
    """Group Base"""
    name = StringField('name',
                       [validators.required(message='name is require.'),
                        validators.length(max=20,
                                          message="name's max len is 20.")])
    tag = StringField('tag',
                      [validators.required(message='tag is require.'),
                       validators.length(max=16,
                                         message="tag's max len is 16.")])

    permissions = StringField('permissions',
                              [validators.optional()])

    @staticmethod
    def validate_tag(_, field):
        """
        validate tag
        :param _:
        :param field:
        """
        if field.data not in Group.TAGS:
            raise ValueError("tag's value is wrong.")

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


class GroupIndexForm(FlaskForm):
    """GroupIndex"""
    NAME = '搜索组'

    endpoints = {'success': '',
                 'failed': 'bp_group.index'}

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
            query = current_session.query(Group)
        else:
            cp = index_dict[self.field.data](value)
            query = current_session.query(Group).filter(cp)

        rows = query.all()
        return rows


class GroupCreateForm(GroupBaseForm):
    """Group Create"""
    NAME = '添加组'

    endpoints = {'success': 'bp_group.index',
                 'failed': ''}

    @staticmethod
    def validate_name(_, field):
        """
        validate name
        :param _:
        :param field:
        """
        if current_session.query(Group).filter_by(name=field.data).first():
            raise ValidationError('name is existed: (%s).' % field.data)


class GroupModifyForm(GroupBaseForm, IdVersionForm):
    """Group Modify"""
    NAME = '编辑组'

    target = Group
    endpoints = {'success': 'bp_group.index',
                 'failed': ''}

    @staticmethod
    def validate_name(form, field):

        """
        validate_name
        :param form:
        :param field:
        """
        row = current_session.query(Group).\
            filter_by(**{'name': field.data}).first()
        if row and row.id != form.id.data:
            raise ValidationError('name is existed: (%s).' % field.data)


class GroupDeleteForm(IdsVersionsForm):
    """Group Delete"""
    NAME = '删除组'

    target = Group
    endpoints = {'success': 'bp_group.index',
                 'failed': 'bp_group.index'}

