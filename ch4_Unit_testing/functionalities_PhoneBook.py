# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:25:17 2019

@author: maria
"""

import sqlite3
import os
from PhoneBook_Project_functions2_from_Muna import *
import requests
from math import sin, cos, sqrt, atan2, radians


def check_db(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False

def get_cursor(environment):
    cursor, connection = connection_factory(environment)
    return cursor, connection

def get_business_type():
    while True:
        try:
            business_type=input("Please specify the business type:\n").title()
            if business_type.isdigit():
                raise character_error

        except Exception as character_error:
            print("Please only use characters.")
        except Exception:
            print("That business type is not valid, please try again.")
        else:
            print (business_type)
            return business_type
        
            
def check_if_input_business_type_is_in_database():  
    cursor, connection = connection_factory("mariana")
    while True:
        try:
            business_type=get_business_type()
            if business_type != None:
#                query = "SELECT business_category FROM businesses WHERE =?"
                cursor.execute("SELECT business_category FROM businesses WHERE business_category=?", (business_type,))
                results = cursor.fetchall()
#                print(results)
#                print(type(results))
                for index in range(len(results)-1):
                    if business_type in results[index]:
                        print("Mariana is the best.")
                        return business_type
                    else:
                        print("Muna is the best!")
                        raise not_in_database

        except Exception as not_in_database:
            print("That is not a valid business type.")
        
#check_if_input_business_type_is_in_database()                        
                
              
def get_input_postcode_and_coordinates_for_input_postcode():
    while True:
        try:
            input_postcode=input("Please specify the postcode:\n")
            input_postcode=input_postcode.replace(" ","")
            endpoint_postcode="https://api.postcodes.io/postcodes/"
            postcode_response=requests.get(endpoint_postcode+input_postcode)
            data_postcode=postcode_response.json()
            if data_postcode['status'] ==200:
                latitude=data_postcode['result']['latitude']
                longitude=data_postcode["result"]["longitude"]
                print(longitude, latitude)
                return longitude, latitude
            else:
                raise postcode_not_valid
                
        except Exception as postcode_not_valid: 
            print("The postcode you provided is not valid!")

def get_information_for_businesses_with_input_business_type():
    cursor, connection = connection_factory("mariana")
    business_type=check_if_input_business_type_is_in_database()
    cursor.execute("SELECT business_name, telephone_number, postcode FROM businesses WHERE business_category=?", (business_type,)) 
    results = cursor.fetchall()
    businesses_info_list=[]
    for row in results:
#        print(row)
        row=list(row)
#        print(type(row))
#        print(row)
        postcode=row[2]
#        print(postcode)
        coordinates=get_coordinates_for_postcode(postcode)
        coordinates=list(coordinates)
#        print(coordinates)
        row.extend(coordinates)
#        print(row)
        businesses_info_list.append(row)
    print(businesses_info_list)
    return businesses_info_list

def get_coordinates_for_postcode(postcode):
    endpoint_postcode="https://api.postcodes.io/postcodes/"
    postcode_response=requests.get(endpoint_postcode+postcode)
    data_postcode=postcode_response.json()
    if data_postcode['status'] ==200:
        latitude=data_postcode['result']['latitude']
        longitude=data_postcode["result"]["longitude"]
#        print(longitude, latitude)
        return longitude, latitude
    else:
        print("The postcode you provided is not valid!")
        
    

def distance():
    businesses_info_list=get_information_for_businesses_with_input_business_type()
    long1,lat1=get_input_postcode_and_coordinates_for_input_postcode()
    for index in range(len(businesses_info_list)-1):
        long2=businesses_info_list[index][3]
        lat2=businesses_info_list[index][4]
        R = 6373.0 # approximate radius of earth in km
        dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        a=abs(a)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        hdist = R * c
        hdist=int(hdist)
        print(hdist)
        print(businesses_info_list[index])
        businesses_info_list[index].append(hdist)
        print(businesses_info_list[index])
    print (businesses_info_list)
    return businesses_info_list 

distance()
