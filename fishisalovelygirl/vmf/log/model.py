#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MySQL"""

from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import TEXT
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

from mysql_engine import Base, engine


class Log(Base):
    """Log
    """

    __tablename__ = 'log'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, default=1)

    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', foreign_keys=[user_id])

    time_ = Column(DateTime, nullable=False)

    form = Column(LONGTEXT)

    message = Column(TEXT)

    def get(self, sn):
        """get data
        """
        data = {'sn': sn,
                'id': self.id,
                'version': self.version,
                'user_id': self.user_id,
                'user': self.user.name,
                'time_': self.time_,
                'message': self.message,
                'form': self.form}
        return data


def init_tables():
    """create table
    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_tables()
