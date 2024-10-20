#Program to plot polar curve circle r=a, a is radius of the circle
from pylab import *
#axes(projection = 'polar')
r=3
rad=[]
theta = arange(0,2*pi,0.01)
#plotting the circle
for i in theta:
    rad.append(r)
    polar(theta, 'g.')
show()