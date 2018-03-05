#!/usr/bin/env python

"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Wordfence (Feedjit)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, _, _ = get_page(get=vector)
        retval = re.search(r"This response was generated by Wordfence", page or "", re.I) is not None
        retval |= re.search(r"Your access to this site has been limited", page or "", re.I) is not None
        if retval:
            break

    return retval