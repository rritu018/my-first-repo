#Program to plot lemniscate - an implicit function
from sympy import *
from pylab import *

x,y = symbols('x y')

p2=plot_implicit(Eq(4*(y**2),(x**2)*(4-x**2)),(x,-5,5),(y,-5,5),xlabel=False,ylabel=False,titles='Lemniscate : $a^2 y^2 = x^2 (a^2-x^2), a>0$ ') # a=2