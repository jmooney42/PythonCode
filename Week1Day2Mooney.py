

from matplotlib.pyplot import* 
from numpy import *
t = arange(1,3,0.02)
T = (6*log(t)-7*exp(.2*t))
figure(1)
clf()
plot(t,T)
xlabel('Time (min.)')
ylabel('Temp (C)')
title('Mooney-Plot')
show()
disp('Hello World! I just wrote my first Python program. Yayyyyyyyy \nJoseph Mooney')