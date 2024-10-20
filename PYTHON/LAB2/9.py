#Program to plot functions x, x^2 and X^3 for same values of x
from pylab import *
x= arange (0 , 2 , 0.001 )
y1=x
y2=x**2
y3=x**3
plot(x,y1) # Plot of y=x a linear curve
plot(x,y2) # Plot of y=x^2 a quadric curve
plot(x,y3) # Plot of y=x^3 a cubic curve
xlabel('x axis ') # Add an x- label to the axes .
ylabel('y axis ') # Add a y- label to the axes .
title(" Simple Plot ") # Add a title to the axes .
show() # to show the complete graph