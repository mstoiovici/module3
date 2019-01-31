# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:54:39 2019

@author: maria
"""

def wordcount(data):
    result={}
    words=data.split()
    for word in words:
            print("This word is: ",word)
            if word in result:
                result[word]+=1
                print("wordCount is: ",result[word])
            else:
                result[word]=1
                print("wordCount is: ",result[word])
    print("Result is now",result)
    return result

wordcount("foo bar foo ")