#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""user"""

from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from mysql_engine import Base, engine


class User(Base):
    """User"""
    STATUS_BLOCK = 'block'
    STATUS_ACTIVE = 'active'

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, default=1)

    w_id = Column(String(16), unique=True, nullable=False)
    password = Column(String(64))

    name = Column(String(20), nullable=False)

    email = Column(String(64), unique=True, nullable=False)

    group_id = Column(Integer, ForeignKey('group.id'))

    group = relationship('Group', back_populates='users')

    role_apply = Column(String(16), nullable=False)

    status = Column(String(16), nullable=False, default=STATUS_BLOCK)

    def get(self, sn):
        """get
        """
        data = {'sn': sn,
                'id': self.id,
                'version': self.version,
                'w_id': self.w_id,
                'password': self.password,
                'name': self.name,
                'email': self.email,
                'group': self.group.name,
                'group_id': self.group_id,
                'role_apply': self.role_apply,
                'status': self.status}
        return data

    @staticmethod
    def is_authenticated():
        """is authenticated
        """
        return True

    def is_active(self):
        """is active
        """
        return False if self.status == self.STATUS_BLOCK else True

    @staticmethod
    def is_anonymous():
        """is anonymous
        """
        return False

    def get_id(self):
        """get_id
        """
        return self.id

    def __repr__(self):
        """__repr__
        """
        return self.name


def init_tables():
    """create table
    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
