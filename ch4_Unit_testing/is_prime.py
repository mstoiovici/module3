# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:20:44 2019

@author: maria
"""

# this script checks if a given inpute number is a prime numaber

def is_prime(number):
    for num in range(2,number):
        #print(num)
        
        if number%num==0:
            return False
            
    return True

#print(is_prime(10))