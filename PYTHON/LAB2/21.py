#Program to plot De-cartes  - an implicit function
from sympy import *
from pylab import *

x,y = symbols('x y')

p2=plot_implicit(Eq(x ** 3+y ** 3,3*2*x*y),(x,-5,5),(y,-5,5),xlabel=False,ylabel=False,
 title='Folium of De-cartes : $x^3 + y^3 = 3 a x y, a> 0$ ') # r= 2