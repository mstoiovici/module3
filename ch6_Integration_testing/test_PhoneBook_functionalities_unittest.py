# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:54:12 2019

@author: maria
"""

import unittest
import sqlite3
from PhoneBook_functionalities import *
#from PhoneBook_Project_functions2_from_Muna import *

class Test_Phonebook(unittest.TestCase):
    def test_dbs(self):
        self.assertTrue(check_db("blah_blah_phoneBookProject.db"))
    def test_get_cursor(self):
        self.assertTrue(get_cursor("blah_blah"))
               
        
if __name__=="__main__":
    unittest.main() 