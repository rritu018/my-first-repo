#Program to plot parametric curve - circle
from pylab import *
r=float(input("enter the radius of the circle: "))
theta=arange(0,2*pi,0.01)
x=r*cos(theta)
y=r*sin(theta)
plot(x,y) # plot using matplotlib . piplot
axis('square')
show() # show the plot