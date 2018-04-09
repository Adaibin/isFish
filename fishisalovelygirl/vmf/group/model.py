#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MySQL"""

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Column
from sqlalchemy import Integer

from sqlalchemy.orm import relationship

from mysql_engine import Base, engine


class Group(Base):
    """Group"""

    __tablename__ = 'group'

    TAG_TEST = 'test'
    TAG_DEV = 'dev'
    TAG_OPS = 'ops'
    TAG_DBA = 'dba'
    TAG_PM = 'pm'
    TAG_ADMIN = 'admin'

    TAGS = (TAG_TEST, TAG_DEV, TAG_OPS, TAG_DBA,
            TAG_PM, TAG_ADMIN)

    id = Column(Integer, primary_key=True)
    version = Column(Integer, default=1)
    #
    name = Column(String(32), unique=True, nullable=False)
    #
    permissions = Column(Text)
    #
    tag = Column(String(16), nullable=False)
    #
    users = relationship('User', back_populates='group')

    def get(self, sn):
        """get
        """
        data = {'sn': sn,
                'id': self.id,
                'version': self.version,
                'name': self.name,
                'permissions': self.permissions,
                'tag': self.tag,
                'users': [u.name for u in self.users]}
        return data


def init_tables():
    """init tables
    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
