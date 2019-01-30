# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:15:59 2019

@author: maria
"""

def passwordCheckAttempt1(truePasscode):
    """
    takes only one parameter:truePasscode
    checks the password from the user to be the true password from the database- given here when calling the main function DataBundlePurchase
    """
    attempt1=input("Please enter your password: ")
    if attempt1==truePasscode:
        return True
    else:
        giveMoreAttemptsToCheckPassword(truePasscode)
        
def giveMoreAttemptsToCheckPassword(truePasscode):
    """
    takes only one parameter:truePasscode
    gives 2 other attempts to user to give the right passcode
    """
    attempt2=input("Please enter your password for the second time: ")
    if attempt2==truePasscode:
        return True
    else:
        attempt3=input("Please enter your password for the third time: ")
        if attempt3==truePasscode:
            return True
        else:
            return False        


print(round(2.2751,1))
print(round(20.897+5.23, 2))