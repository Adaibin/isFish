#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MySQL"""

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Column
from sqlalchemy import Integer

from sqlalchemy.orm import relationship

from mysql_engine import Base, engine


class M1(Base):
    """M1"""

    __tablename__ = 'm1'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, default=1)
    # 组名
    name = Column(String(20), unique=True, nullable=False)
    # 权限
    permissions = Column(Text)
    # 组用户
    users = relationship('User', back_populates='group')


def init_tables():
    """创建表"""
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
