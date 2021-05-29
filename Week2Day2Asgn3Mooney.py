# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:03:57 2021

@author: joseph Mooney
"""
from matplotlib.pyplot import* 
from numpy import *
t= arange(0,1,0.01)
y = 2.0*sin(2*pi*t)
N = len(y)


def my_plot(t,y_sat,y,x_label = '', y_label = '',name = '',fig_num=0,cl_fig =True):
    if fig_num:
        figure(fig_num)
    if cl_fig:
        clf()
    plot(t,y,'r--')
    plot(t,y_sat)
    if x_label:
        xlabel(x_label)
    if y_label:
        ylabel(y_label)
    if name:
        title(name)
   
# First Method
y_sat1 = zeros(N)
for i in range(N):
    y_i = y[i]
    if y_i<.5:
        y_sat1[i]=0
    else:
        y_sat1[i]=y_i
my_plot(t,y_sat1,y,x_label='Time (s)',y_label='$y(t)$',name='Mooney 1',fig_num=1)

# Second Method
y_sat2 = zeros(N)
for i, y_i in enumerate(y):
    if y_i < .5:
        y_sat2[i]=0
    else:
        y_sat2[i]=y_i
my_plot(t,y_sat2,y,x_label='Time (s)',y_label='$y(t)$',name='Mooney 2',fig_num=2)

# Third Method
import copy
y_sat3 = copy.copy(y)
y_sat3[y_sat3 < .5] = 0
my_plot(t,y_sat3,y,x_label='Time (s)',y_label='$y(t)$',name='Mooney 3',fig_num=3)

# Fourth Method
import copy
y_sat4 = copy.copy(y)
inds1 = where(y<.5)[0]
y_sat4[inds1]=0
my_plot(t,y_sat4,y,x_label='Time (s)',y_label='$y(t)$',name='Mooney 4',fig_num=4)

show()