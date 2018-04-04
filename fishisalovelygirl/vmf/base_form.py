# -*- coding: utf-8 -*-
"""base form"""
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import IntegerField
from wtforms import StringField
from wtforms import ValidationError

from flask_sqlalchemy_session import current_session


class IdsVersionsForm(FlaskForm):
    """IdsVersionsForm
    """
    ids = StringField('ids',
                      [validators.input_required(
                          message='ids is require.')])
    versions = StringField('versions',
                           [validators.input_required(
                               message='versions is require.')])

    def validate_ids(self, _):
        """
        validate ids
        :param _:
        :return:
        """
        if 'target' not in self.__class__.__dict__:
            return True
        class_ = self.__class__.target

        ids_versions = self.get_ids_versions()

        for id_version in ids_versions:
            filter_ = {'id': id_version['id'],
                       'version': id_version['version']}
            row = current_session.query(class_).\
                filter_by(**filter_).first()
            if not row:
                raise ValidationError('id-version is out date, pls update page.')

    def get_ids_versions(self):
        """
        get ids/versions
        :return:
        """
        ids = self.ids.data.replace(' ', '').split(',')
        versions = self.versions.data.replace(' ', '').split(',')
        if len(ids) != len(versions):
            raise ValidationError('len(id) != len(version).')

        if list(filter(lambda x: not x.isnumeric(), ids)):
            raise ValidationError('id must be numeric.')
        if list(filter(lambda x: not x.isnumeric(), versions)):
            raise ValidationError('version must be numeric.')

        # convert '2,3' & '1,1' to [{id:2,version:1}, {id:3,version:1}]
        ids_versions = zip(ids, versions)
        ids_versions = [{'id': int(idv[0]),
                         'version': int(idv[1])} for idv in ids_versions]
        return ids_versions


class IdVersionForm(FlaskForm):
    """IdVersionForm
    """
    id = IntegerField('id', [validators.required(
        message='id is require.')])
    version = IntegerField('version', [validators.required(
        message='version is require.')])

    def get_id_version(self):
        """get_id_version
        """
        return {'id': self.id.data, 'version': self.version.data}

    def increase_version(self, data=None):
        """
        increase_version
        :param data:
        :return:
        """
        data = self.data_parser() if not data else data
        class_ = self.__class__.target
        id_ = data['id']
        row = current_session.query(class_).filter_by(id=id_).first()
        data['version'] = row.version + 1
        return data

    def validate_id(self, _):
        """
        validate_id
        :param _:
        """
        filter_ = {'id': self.id.data, 'version': self.version.data}

        class_ = self.__class__.target
        if not current_session.query(class_).filter_by(**filter_).first():
            raise ValidationError('id-version is out date, pls update page.')


class IndexBaseForm(FlaskForm):
    """IndexBaseForm
    """
    field = StringField('field',
                        [validators.required(message='field is require.'),
                         validators.length(max=20,
                                           message="field's max len is 20.")])

    value = StringField('value',
                        [validators.optional(),
                         validators.length(max=128,
                                           message="value's max len is 128.")])
