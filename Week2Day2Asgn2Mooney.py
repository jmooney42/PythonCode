# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:03:57 2021

@author: joseph Mooney
"""
from numpy import *
Hours = int(input("Please enter the number of hours:"))
disp('The number of hours worked is:')
disp(Hours)
RPH = int(input("Please enter the rate per hour:"))
disp('The pay rate per hour is ')
disp(RPH)
def computepay(a,b):
    if a < 40 :
        pay = a*b
        disp('The amount of money earned in ')
        disp(a)
        disp(' hours is $')
        disp(pay)
    elif a >= 40:
        regpay = 40*b
        overtime = a-40
        overpay = overtime*1.5*b
        pay = regpay+overpay
        disp('The amount of money earned in ')
        disp(a)
        disp(' hours is $')
        disp(pay)
    else:
        disp('The value entered is not valid')
computepay(Hours,RPH)

