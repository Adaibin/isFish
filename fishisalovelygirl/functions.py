# -*- coding: utf-8 -*-
"""functions"""
import hashlib
from datetime import datetime

from app import cache


def url_to_md5(url, update=True):
    """
    translate url to md5
    :param url:
    :param update:
    """
    date = str(datetime.today())
    md5 = hashlib.md5(''.join((url, date)).encode()).hexdigest()

    md5_ = cache.get(url)
    if md5_ != md5 and update:
        cache.set(key=url, value=md5, timeout=60 * 60)
        cache.set(key=md5, value=url, timeout=60 * 60)
    return md5
