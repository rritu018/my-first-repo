#Program to plot exponential function
from pylab import *
n=int(input('Enter the range value for x: '))
x = arange(-n,n,0.0001) # x takes the values between -10 and 10 with a step length of 0.001
y = exp(x) # Exponential function
plot(x,y,'r') # plotting the points
xlabel('x') # naming the x axis
ylabel('$e^x$') # naming the y axis
title(" Exponential curve ") # giving a title to the graph
grid() # displaying the grid
show() # shows the plot