from rosen import rosenbrock
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#main文件调用其他文件里到函数，画二维rosenbrock函数的图像
def main():
    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-4,4,0.25)
    Y = np.arange(-4,4,0.25)
    X,Y = np.meshgrid(X,Y)
    f = rosenbrock(X,Y)
    
    ax.plot_surface(X,Y,f,rstride=1,cstride=1,cmap='rainbow')
    show()
    

if __name__ == '__main__':
     main()
