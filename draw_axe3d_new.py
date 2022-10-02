from turtle import color
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def rosenbrock(x,y):
    a,b = 1,100
    f = (a - x) ** 2 + b * (y - x ** 2) ** 2
    return f

fig = figure()
ax = Axes3D(fig)
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
f = rosenbrock(X,Y)

ax.plot_surface(X,Y,f,rstride=1,cstride=1,cmap='rainbow')

show()