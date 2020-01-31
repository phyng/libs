# coding: utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from unittest import TestCase
from iterlib import uniqify


class IterlibTest(TestCase):

    def test_uniqify(self):
        self.assertListEqual(list(uniqify([1, 2, 3, 3])), [1, 2, 3])
