from __future__ import absolute_import, unicode_literals

import unittest

from mason import Param, ANY, COALESCE


class TheParamClassToStringMethod(unittest.TestCase):
    def test_works(self):
        param = Param('param')

        self.assertEqual(str(param), '%(param)s')
        self.assertEqual(param.__unicode__(), '%(param)s')
        self.assertEqual(param.__str__(), '%(param)s')


class TheAnyClassToStringMethod(unittest.TestCase):
    def test_works(self):
        param = ANY('param')

        self.assertEqual(str(param), 'ANY(param)')


class TheCoalesceClassToStringMethod(unittest.TestCase):
    def test_works(self):
        param = COALESCE('param', 0)

        self.assertEqual(str(param), 'COALESCE(param, 0)')
