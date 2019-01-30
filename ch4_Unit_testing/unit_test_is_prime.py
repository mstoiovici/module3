# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:24 2019

@author: maria
"""

import unittest
from ch4_Mariana import is_prime

import sys
"""
class prime_test(unittest.TestCase):
    ## one function doing both things
    def test_prime(self):
        self.assertIsInstance(sys.argv[0],int)
        self.assertTrue(is_prime(sys.argv[0]))
   
    ### or two separate functions
    #def test_prime(self):
#        self.assertTrue(is_prime(5))
#        
#    def sys_input(self):
#        self.assertIsInstance(sys[1],int)
    def sys_input(self):
       self.assertIsInstance(sys.argv[0],int)
       
if __name__=="__main__":
    unittest.main()
    
"""

class prime_test(unittest.TestCase):
   
    def test_prime(self):
        self.assertTrue(is_prime(5))

if __name__=="__main__":
    unittest.main()