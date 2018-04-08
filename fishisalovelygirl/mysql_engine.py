#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MySQL"""
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql


pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:9fuxaFr4ucMilcf@127.0.0.1/lg',
                       encoding='utf-8',
                       pool_recycle=3600,
                       pool_size=50, max_overflow=0)
session_factory = sessionmaker(bind=engine)

Base = declarative_base()


def to_dict(self):
    """SqlAlchemy instance to dict"""
    dict_ = {}

    for col in self.__table__.columns:
        val = getattr(self, col.name)
        val = str(val) if isinstance(val, (datetime.datetime, datetime.time)) else val
        dict_[col.name] = val
    return dict_


Base.to_dict = to_dict
