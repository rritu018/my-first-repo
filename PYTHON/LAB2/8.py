#program to plot sine and cosine function together with same values of x
from pylab import *
x = arange(-10,10,0.001)
plot(x,sin(x),x,cos(x)) # plotting sine and cosine function together with same values of x
title(" sine curve and cosine curve ")
xlabel(" Values of x")
ylabel(" Values of sin (x) and cos(x) ")
grid()
show()