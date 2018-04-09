#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Properties"""

from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.dialects.mysql import LONGTEXT

from mysql_engine import Base, engine


class Properties(Base):
    """Properties"""

    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, default=1)

    table_ = Column(String(32), nullable=False, unique=True)
    params = Column(LONGTEXT)


def init_tables():
    """create table
    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
