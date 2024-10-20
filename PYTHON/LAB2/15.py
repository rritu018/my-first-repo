#Program to plot parametric curve - cycloid x=r(theta -sin(theta)) and y=r(1 -cos(theta))
from pylab import *
r=4
theta=arange(-2*pi,2*pi,0.01)
x=r*(theta-sin(theta))
y=r*(1-cos(theta))
plot(x,y) 
title("$x=a(\\theta-cos(\\theta)); y=a(1-cos(\\theta))$")
show() # show the plot
