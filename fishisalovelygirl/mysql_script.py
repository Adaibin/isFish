#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""MySQL Script"""

from sqlalchemy.orm import sessionmaker

from mysql_engine import engine


SessionMaker = sessionmaker(bind=engine, autocommit=False, autoflush=False)
