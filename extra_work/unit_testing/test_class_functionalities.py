# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:19:42 2019

@author: maria
"""

import unittest
from class_functionalities import Employee

class TestEmployee(unittest.TestCase):
#
#    @classmethod
#    def setUpClass(cls):
#        print('setupClass')
#
#    @classmethod
#    def tearDownClass(cls):
#        print('teardownClass')
#
#    def setUp(self):
#        print('setUp')
#        self.emp_1 = Employee('Corey', 'Schafer', 50000)
#        self.emp_2 = Employee('Sue', 'Smith', 60000)
#
#    def tearDown(self):
#        print('tearDown\n')

    def test_email(self):
        emp_1=Employee("Corey","Schafer", 20000)
        emp_2=Employee("Sue","Smith", 25000)
        #print('test_email')
        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')
        
        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        emp_1=Employee("Corey","Schafer", 20000)
        emp_2=Employee("Sue","Smith", 25000)
        #print('test_fullname')
        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')
#
    def test_apply_raise(self):
        emp_1=Employee("Corey","Schafer", 20000)
        emp_2=Employee("Sue","Smith", 25000)
        #print('test_apply_raise')
        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 21000)
        self.assertEqual(emp_2.pay, 26250)
        
        
if __name__ == '__main__':
    unittest.main()
