# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:59:41 2019

@author: maria
"""

#f=open("testfile") #### if you run this you'l get an error--> FileNotFoundError: [Errno 2] No such file or directory: 'testfile'
try:
    f=open("testfile")
except Exception:
    print("Error!")   ##### if you run this it's going to print --> Error!


try:
    f=open("testfile")
except Exception as e:
    print(e)   ##### if you run this it's going to print --> [Errno 2] No such file or directory: 'testfile'



print("------------Task1 - Print out exception as detected-----------")
print("-----in this exp you'll get the error-----------")
try:
    f=open("testfile")
except Exception:
    print("Sorry, this file doesn not exist, or the file name is wrong. please check again.")


print("-----in this exp you'll woun't get the error-----------")
try:                          #####once you correct your code, you won't get an error anymore
    f=open("testfile.txt")
except Exception:
    print("Sorry, this file doesn not exist, or the file name is wrong. please check again.")


print("------------------Task2 specific excepsions before general exceptions-----------------")
try:
    f=open("testfile.txt")
    s1=not_exists
except Exception: 
    print("Sorry, this file doesn not exist, or the file name is wrong. please check again.")              ##### if you run this it's like saying: try this and if anything else happens then print the else(the exception, which is an error)
    
try:      
    f = open('testfile.txt') 
    #s1 = not_exist 
except FileNotFoundError: 
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.") 

try:
   f = open('testfile.txt') 
   s1 = not_exsit
except FileNotFoundError: 
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.") 
except Exception: 
    print("Sorry. Something is wrong after opening function.") 
 





print("------------------Task3 -----------------")
try:                         ####try to open this file
    f=open("testfile.txt")
    s1=not_exists
except Exception as e:       ####if something wrong happens(an error), print that error
    print(e)


print("------------------Task4 Else block -----------------")

try:                         ####try to open this file
    f=open("testfile.txt")
    s1=not_exists
except Exception as e:       ####if something wrong happens(an error), print that error
    print(e)
else:                       ####else if nothing wrong happens(there is no exception), do this
    print(f.read())
    f.close()


print("------------------Task5 - Finally block-----------------")

try:
    f=open("testfile")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")
    
print("------")
try:
    f=open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")
    


print("--------Task6 - Manually raise an exception--------------") 
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt': 
        raise Exception
except Exception as e:
    print('file name are the same') 