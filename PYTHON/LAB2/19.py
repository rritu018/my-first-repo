#Program to plot Cissiod - an implicit function
from sympy import *
from pylab import *

x,y = symbols('x y')

p2=plot_implicit(Eq ((y**2)*(3-x),x**3),(x,-2,5),(y,-5,5),title = 'Cissiod : $y^2 (a-x)=x^2  (a+x), a> 0$ ') #r=2