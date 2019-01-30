# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:41:51 2019

@author: maria
"""
"""
import unittest
from is_prime import is_prime



class PrimesTest(unittest.TestCase):
    def test_prime_float(self):
        self.assertTrue(is_prime(4))

if __name__=="__main__":
    unittest.main()
    
"""

import unittest
from is_prime import is_prime
import sys



class PrimesTest(unittest.TestCase):      ############# this returns errors
    def test_prime_float(self):
        self.assertTrue(is_prime(sys.argv[0]))

if __name__=="__main__":
    unittest.main()