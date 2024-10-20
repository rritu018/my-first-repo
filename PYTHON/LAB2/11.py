 #Plot cardioid r=5(1+cos theta )
from pylab import *
theta=linspace(0,2*pi,1000)
r1=5*(1+cos( theta ))
polar(theta,r1,'r')
show()
