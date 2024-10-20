#Program to plot functions x, x^2 and X^3 for same values of x
from pylab import *
x= arange (0 , 2 , 0.001 )
plot(x,x,label='linear ') # Plot of y=x a linear curve
plot(x,x**2,label='quadratic ') # Plot of y=x^2 a quadric curve
plot(x,x**3,label='cubic ') # Plot of y=x^3 a cubic curve
xlabel('x axis ') # Add an x- label to the axes .
ylabel('y axis ') # Add a y- label to the axes .
title(" Simple Plot ") # Add a title to the axes .
legend(loc='upper right') # Add a legend
show() # to show the complete graph