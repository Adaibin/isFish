# -*- coding: utf-8 -*-
"""lovely girl"""

from app import lg
from blueprints import register_bp


register_bp(lg)

if __name__ == '__main__':
    lg.run(host='192.168.4.214', port=9755)
