#Program to plot scatter points
# importing the required module
from pylab import *
x = [1,2,3,4,6,7,8]
y = [2,7,9,1,5,10,3]
scatter (x,y,color='red')
xlabel ('x-axis')
ylabel ('y-axis')
title ('scatter points')
grid()
show() #function to show the plot