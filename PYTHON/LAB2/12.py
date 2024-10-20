# Plot cardioids r=5(1+cos( theta )) and r=5(1-cos (theta) )
from pylab import *
theta=linspace(0,2*pi,1000)
r1=5+5*cos(theta)
r2=5-5*cos(theta)
polar(theta,r1,label='r=5(1+cos( theta ))')
polar(theta,r2,label='r=5(1-cos (theta))')
title("$r=5(1+cos(\\theta)); r=5(1-cos(\\theta))$")
legend()
show()
