# a = 1
# b = 1
# c = a + b
# print("a is: %2d ," % a, "b is: %2d ," % b, "the result of a + b is : %2d" % c)


from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
def rosenbrock(x,y):
    f = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    return f
# a,b = 1,2

fig = figure()
ax = Axes3D(fig)
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
f = rosenbrock(X,Y)
# a,b = 1,1
# print("the result is : %.4f" % f)
ax.plot_surface(X,Y,f,rstride=1,cstride=1,cmap='rainbow')
# scatter(a,b,color='black')
show()