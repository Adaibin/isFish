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


def init_tables():
    """init tables
    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
