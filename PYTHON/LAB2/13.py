# Plot Four Leaved Rose r=2 | cos2x |
from pylab import *
x=linspace(0,2*pi,1000 )
r=2*abs(cos(2*x))
polar(x,r,'r')
show()