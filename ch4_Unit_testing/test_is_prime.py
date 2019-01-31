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
"""
import unittest
from is_prime import is_prime
import sys



class PrimesTest(unittest.TestCase):      ############# this returns errors
    def test_prime_float(self):
        self.assertTrue(is_prime(sys.argv[0]))

if __name__=="__main__":
    unittest.main()
"""

import unittest
from is_prime import *

class IsPrimeTest(unittest.TestCase):
    """
    Tests for is_prime()
    """
    
    def test_is_five_prime(self):
        """Is five successfully determined to be prime?
        """
        self.assertTrue(is_prime(5))
    
    def test_is_zero_not_prime(self):
        """is zero correctly determined not to be prime?
        """
        self.assertFalse(is_prime(0)) # we'll get a Fail for this test since True is not false
        
    def test_is_four_non_prime(self):
        """is four correctly determined not to be prime?
        """
        #self.assertTrue(is_prime(4),msg="Four is not prime!")# this raises an error and gives us the msg :"Four is not prime!"
        self.assertFalse(is_prime(4),msg="Four is not prime!")# this will pass the test
        self.assertFalse(is_prime(4))
        

    def test_print_next_prime(self):
        self.assertTrue(print_next_prime(5))
        self.assertTrue(print_next_prime(7))
        self.assertTrue(print_next_prime(6))
    
    def test_negative_numver(self):
        """is a negative number correctly determined not to be prime?
        """
        for index in range(-1,-10,-1):
            self.assertFalse(is_prime(index),msg="{} should not be determined to be prime".format(index))
            
        
if __name__== "__main__" :
    unittest.main()
        