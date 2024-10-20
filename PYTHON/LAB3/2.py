#Program to plot exponential function y = e^x
from pylab import *
x = arange(-5,5,0.001)
y = exp(x)
plot(x,y)
title("$ y=e^x $")
grid()
xlabel("x-axis")
ylabel("y-axis")
xlim(-5,5)
ylim(-1,20)
axvline(x=0, color = "red")
axhline(y=0, color = "red")
show()