# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:58:53 2019

@author: maria
"""

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        raise ValueError("can not divide by zero!")
    return x/y




