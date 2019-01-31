# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:58:52 2019

@author: maria
"""

from practice2 import wordcount
import unittest

class TestUnit(unittest.TestCase):
    def test_wordcount(self):
        self.assertDictEqual({'foo': 2, 'bar': 1}, wordcount("foo bar foo "))