#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPL v3 Copyright: 2019, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

class Test(unittest.TestCase):

def find_tests():
    return unittest.defaultTestLoader.loadTestsFromTestCase(Test)
