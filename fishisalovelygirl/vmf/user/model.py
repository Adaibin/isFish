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

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, default=1)

    name = Column(String(20), nullable=False)

    group_id = Column(Integer, ForeignKey('group.id'))

    group = relationship('Group', back_populates='users')


def init_tables():
    """创建表"""
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
