from matplotlib.pyplot import *
from numpy import *
t = arange(1,3,0.02)
T = 6*log(t)
figure(1)
clf()
plot(t,T)
xlabel(’Time (min.)’)
ylabel(’Temperature (C)’)
show()
