# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:59:16 2019

@author: maria
"""

import unittest 
import functionalities

class TestCalc(unittest.TestCase):
    def test_add(self):
        #result=functionalities.add(10,5)
        self.assertEqual(functionalities.add(10,5),15)
        self.assertEqual(functionalities.add(3,7),10)
        self.assertEqual(functionalities.add(-2,5),3)
        self.assertEqual(functionalities.add(-2,-3),-5)
        
    def test_subtract(self):
        #result=functionalities.add(10,5)
        self.assertEqual(functionalities.subtract(10,5),5)
        self.assertEqual(functionalities.subtract(3,7),-4)
        self.assertEqual(functionalities.subtract(-2,5),-7)
        self.assertEqual(functionalities.subtract(-2,-3),1)
     
    def test_divide(self):
        self.assertEqual(functionalities.divide(10,5),2)
        #self.assertRaises(ValueError,functionalities.divide,10,0)
        with self.assertRaises(ValueError):
            functionalities.divide(10,0)
    
        
if __name__=="__main__":
    unittest.main()