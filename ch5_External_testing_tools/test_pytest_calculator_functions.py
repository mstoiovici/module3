# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:32:34 2019

@author: maria
"""

import pytest

from calculator_functions  import *
def test_add_function_returns_correct_result():
    assert (add(2,2)) == 4


def test_subtract_function_returns_correct_result():
    assert (subtract(2,2)) == 0
    assert (subtract(7,2)) == 5
    
def test_multiply_function_returns_correct_result():
    assert (multiply(2,3)) == 6
    assert (multiply(7,2)) == 14
    
def test_divide_function_returns_correct_result():
    assert (divide(6,2))==3
    
    
