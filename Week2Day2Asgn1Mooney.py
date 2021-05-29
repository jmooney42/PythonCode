# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:24:09 2021

@author: joseph Mooney
"""
from numpy import *
Hours = int(input("Please enter the number of hours:"))
disp('The number of hours worked is:')
disp(Hours)
RPH = int(input("Please enter the rate per hour:"))
disp('The pay rate per hour is ')
disp(RPH)
if int(Hours) in range(40,168) :
    avgpay = 40*RPH
    overtime = Hours-40
    overpay = overtime*1.5*RPH
    pay = avgpay+overpay
    disp('The amount of money earned for the week is:')
    disp(pay)
elif Hours < 40 :
    pay = Hours*RPH
    disp('The amount of money earned for the week is:')
    disp(pay)
else:
    disp('This is not a valid input please enter a positive value less than or equal to 168')
