# -*- coding: utf-8 -*-
"""lg"""
import hashlib
from datetime import datetime

from flask import redirect

from app import lg, cache
from blueprints import register_bp


register_bp(lg)


@lg.route('/vmf/md5/<string:md5>',
          methods=['GET', 'POST'],
          endpoint='md5')
def md5_to_url(md5):
    """translate md5 to url
    """
    url = cache.get(md5)
    if not url:
        #todo: md5 is invalid
        return 'md5 is invalid: %s' % md5
    return redirect(url)


if __name__ == '__main__':
    lg.run(host='192.168.4.214', port=9755)
