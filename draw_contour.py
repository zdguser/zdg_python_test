from turtle import color
from pylab import *
import numpy as np

def rosenbrock(x,y):
    f = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    return f
n = 256
x= np.linspace(-1,1.1,n)
y = np.linspace(-0.1,1.1,n)
#生成网格数据
X,Y = np.meshgrid(x,y)
f = rosenbrock(X,Y)

a,b = 1,1


#绘制等高线的颜色，8是几等分
contourf(X, Y, f, 5, alpha=0, cmap='hot')

#绘制等高线
C = contour(X,Y,f,10,color='black',linewidth=0.1)
scatter(a,b,color='black')
show()
