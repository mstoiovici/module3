# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:23:28 2019

@author: maria
"""

#print("--------Task1 - ask the user for an input----")
#
#print("----ask a user for age on a new line---")
#print("What's your age?")
#age=input()
#print("----ask a user for age with a space---")
#age=input("What's your age? ")
#
#print("--------Task2 - cast the last coding age to int data type----")
#
#print("----ask a user for age on a new line---")
#print("What's your age?")
#age=int(input())
#type(age)
#
#print("----ask a user for age with a space---")
#age = int(input("What’s your age? "))
#
#print("----or cast the variable---")
#age=input("what's your age? ")
#age_int=int(age)


#print("-------Task 3: Try the code below  -----------")
#option = input("Please input yes or no ").lower() 
#print(option)


print("-------Task 4 -Checking input  -----------")
print("--using while true infinite loop--")
def checking_input():
    print("***choice***")
    print("1. Display my name") 
    print("2. Display my age") 
    print("3. Display my city") 

    choice=int(input("what's your choice? "))
 
    if choice == 1:
        print("Mrs Mariana")
    elif choice == 2:
        print("33 yrs old")
    elif choice == 3:
        print("London")
    else:
        print("else statement")
        

        
#checking_input()

print("----how to validate the user input----")

def checking_input_one():
    print("***choice***")
    print("1. Display my name") 
    print("2. Display my age") 
    print("3. Display my city") 

    choice=int(input("what's your choice? "))
 
    if choice == 1:
        print("Mrs Mariana")
    elif choice == 2:
        print("33 yrs old")
    elif choice == 3:
        print("London")
    else:
        while choice<1 or choice >3:
            choice=int(input("what's your choice? "))
            if choice == 1:
                 print("Mrs Mariana")
            elif choice == 2:
                print("33 yrs old")
            elif choice == 3:
                print("London")   
            else:
                print("you keep giving a choice outside the options")
        
#checking_input_one()
        
print("----handling errorful input----")
def checking_input_two():
    print("***choice***")
    print("1. Display my name") 
    print("2. Display my age") 
    print("3. Display my city") 
    choice=int(input("what's your choice? "))
    if choice == 1:
        print("Mrs Mariana")
    elif choice == 2:
        print("33 yrs old")
    elif choice == 3:
         print("London")
    else:
        while True:
            try:
                while choice<1 or choice >3:
                    choice=int(input("what's your choice? "))
                    if choice == 1:
                        print("Mrs Mariana")
                    elif choice == 2:
                        print("33 yrs old")
                    elif choice == 3:
                        print("London")
                    else:
                        pass
                break
            except ValueError:
                print("please type a number! ")

def checking_input_two_improved():
    print("***choice***")
    print("1. Display my name") 
    print("2. Display my age") 
    print("3. Display my city") 
    
    while True:
        choice=0
        try:
            while choice<1 or choice >3:
                choice=int(input("what's your choice? "))
            break
        except ValueError:
            print("please type a number! ")
        
    if choice == 1:
        print("Mrs Mariana")
    elif choice == 2:
        print("33 yrs old")
    elif choice == 3:
        print("London")

checking_input_two_improved()  
            
def checking_input_three():          ##### but how to stop after you get all three? this could be a fourth function
    """
    how to keep asking the choice so that you can receive all three answers. 
    """
    print("***choice***")
    print("1. Display my name")
    print("2. Display my age")
    print("3. Display my city")
    choice=0

    while True:
        try:
            while choice<1 or choice >3:
                choice=int(input("what's your choice? "))
                while True:
                    if choice == 1:
                        print("Mrs Mariana")
                    elif choice == 2:
                        print("33 yrs old")
                    elif choice == 3:
                        print("London")
                    else:
                        pass
                    choice=int(input("what's your choice? "))
            break
        except ValueError:
            print("please type a number! ")
                
        
#checking_input_two()               
#checking_input_two_improved()
#checking_input_three()              
                
print("---Task7 -Further on validation- class-based user input validation")
class Spam(object):
    def __init__(self,description,value):
        if not description or value <= 0: ##### if you do not raise this exception, you'll be able to create Ana object, but that one might not be what you want, since Ana object has no description and a negative value 
            raise ValueError
        self.description = description
        self.value = value

#Mari=Spam("Mari",5)
#print(Mari.value)
#Ana=Spam("",-1) ###### this will return a ValueError because you raised that Exception when you defined the class

print("----------write the code with assert statements--------")
class Spam(object):
    def __init__(self, description, value):         
        assert description != ""         
        assert value > 0         
        self.description = description         
        self.value = value 
#Mari=Spam("Mari",5)
#Ana=Spam("",4)  ### this will give you the exact error : assert description != ""
#Ana=Spam("Ana",-1) ### this will give you the exact error : assert value > 0