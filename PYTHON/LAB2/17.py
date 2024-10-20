#program to plot circle - an implicit function
from sympy import *
from pylab import *

x,y = symbols('x y')

p1 = plot_implicit(Eq(x**2 + y**2,4),(x,-4,4),xlabel=False,ylabel=False,title='circle : $x^2+y^2=4$ ' , aspect_ratio=(2.1))

