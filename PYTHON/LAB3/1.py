from pylab import *
x=[2,3,4,5,7]
y=[4,2,3,7,9]
if len(x) !=len(y):
    print("number of values of x and y doesnot match")
else:
    scatter(x,y)
    plot(x,y)
    grid()
    xlabel("x-axis")
    ylabel("y-axis")
    title("curve connecting the given points")
    axvline(x=0,color="red")
    axhline(y=0,color="red")
    show()