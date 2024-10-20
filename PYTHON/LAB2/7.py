#program to plot sine and cosine function together with same values of x
from pylab import *
x = arange(-10,10,0.0001)
y1= sin(x)
y2= cos(x)
plot(x,y1,x,y2) # plotting sine and cosine function together with same values of x
title(" sine curve and cosine curve ")
xlabel("x")
ylabel(" sin (x) and cos(x) ")
grid()
show()