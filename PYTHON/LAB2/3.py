#program to plot scatter points
#importing from the required module
from pylab import *
n=int(input("Enter the number of points : "))
x=[]
y=[]
for i in range(n) :
    a=int(input(f'enter the value of x{i+1} : '))
    x.append(a)
    b=int(input(f'enter the value of y{i+1} : '))
    y.append(b)
    scatter (x,y)
    xlabel ('x-axis')
    ylabel ('y-axis')
    title ('scatter points')
    show()