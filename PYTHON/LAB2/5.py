#Program to plot line graph
# importing the required module
from pylab import *
n=int(input("Enter the number of points : "))
x=[]
y=[]
for i in range(n):
    a=int(input(f'Enter the value of x[{i+1}] :' ))
    x.append(a)
    b=int(input(f'Enter the value of y[{i+1}] : '))
    y.append(b)
    plot(x,y,'r+--')
xlabel('x-axis')
ylabel('y-axis')
title('Line Graph')
show()