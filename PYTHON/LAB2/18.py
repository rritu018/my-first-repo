#Program to plot Strophoid - an implicit function
from sympy import *
from pylab import *

x,y = symbols('x y')

p2 = plot_implicit(Eq((y**2)*(2-x),(x**2)*(2+x)),(x,-3,3),(y,-4,4),xlabel=False,ylabel=False,title='strophoid : $y^2 (a-x)=x^2 (a+x),a>0$ ') #r=2