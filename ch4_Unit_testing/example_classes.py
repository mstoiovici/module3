# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:04:00 2019

@author: maria
"""
"""
class Person(self,name,age,gender):
    
    def name(self):
        self.name=name
"""      
    
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
     
    def getDetails(self):
        print("details : ",self.name,self.age,self.gender)
        
    def changeName(self,newName):
        self.name=newName
    
    def tenPercentLess(self,salary):
        self.newSalary=salary-(salary*0.10)
      
if __name__=="__main__":
   aminat=Person("Aminat",20,"female")
   aminat.getDetails()
   aminat.changeName("Aminat2")
   aminat.getDetails()
    
   
   