#Jason Wiltjer Assignment 3

from matplotlib.pyplot import *
from numpy import *

t= arange(0,1,0.01)
y=2*sin(2*pi*t)

N =  len(y)
i=0

while i<N:
    if -0.5<y[i]<0.5:
        y[i]=0
    i=i+1


plot(t,y)
