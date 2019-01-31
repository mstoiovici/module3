# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:20:44 2019

@author: maria
"""

# this script checks if a given inpute number is a prime numaber
#step1 -we'll get an error out of our test, because num will be 0 at first and we'll divide a number to 0
#def is_prime(number):
#    for num in range(number):
#        #print(num)
#        
#        if number%num==0:
#            return False
#            
#    return True
#print(is_prime(10))


#step2 -- we'll get a *.* out of our test, because we're testing if 5 is a prime number, and 5 %2 is not going to be 0, so the if condition won't be met, so it's going to return True
#def is_prime(number):
#   
#    for num in range(2,number):
#        #print(num)
#        
#        if number%num==0:
#            return False
#            
#    return True

#step3
#def is_prime(number):  
#    if number in (0,1):
#        return False
#    else:
#        for num in range(2,number):
#            #print(num)
#        
#            if number%num==0:
#                return False
#            
#    return True
#step4
#def is_prime(number):
#    if number <0:
#        return False
#    
#    elif number in (0,1):
#        return False
#    else:
#        for num in range(2,number):
#            #print(num)
#        
#            if number%num==0:
#                return False
#            
#    return True

#step5
def is_prime(number):
    if number <=1:
        return False
    

    for num in range(2,number):
        #print(num)
        
        if number%num==0:
            return False
            
    return True


def print_next_prime(number):
    """
    Print the closest prime number larger than *number*
    """
    index= number
    while True:
        index+=1
        if is_prime(index):
            #print(index)
            return True
            