#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:54:04 2019

@author: maria
"""

import unittest
import calculator_functions 


class TddInPythonExample(unittest.TestCase):
    def test_calculator_add_function_returns_correct_result(self):
        self.assertEqual(4,calculator_functions.add(2,2))
        self.assertEqual(1,calculator_functions.add(-1,2))
        self.assertEqual(-3,calculator_functions.add(0,-3))
        
    def test_calculator_subtract_function_returns_correct_result(self):
        self.assertEqual(-1,calculator_functions.subtract(0,1))
        self.assertEqual(1,calculator_functions.subtract(2,1))
        self.assertEqual(1,calculator_functions.subtract(-1,-2))
        
    def test_calculator_multiply_function_returns_correct_result(self):
        self.assertEqual(0,calculator_functions.multiply(0,1))
        self.assertEqual(6,calculator_functions.multiply(2,3))
        self.assertEqual(2,calculator_functions.multiply(-1,-2))
    
    def test_calculator_divide_function_returns_correct_result(self):
        self.assertEqual(calculator_functions.divide(10,5),2)
        #self.assertRaises(ValueError,calculator_functions.divide,10,0)
        with self.assertRaises(ValueError):  #--> 
            calculator_functions.divide(10,0)
        
if __name__=="__main__":
    unittest.main()
        
    