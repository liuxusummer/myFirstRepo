#画三叶草

from numpy import *
from matplotlib.pyplot import *
t=arange(0,2*pi,0.02)
subplot(111,polar=True)
w=sin(3*t)
plot(t,w,'g')
show()



