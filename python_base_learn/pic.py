import matplotlib.pyplot as plt
import numpy as np
# x = np.linspace(-np.pi,np.pi,25,endpoint=True)
# y = np.sin(x) * np.cos(x) + 5
x = np.random.normal(0,1,50)
y = np.random.normal(0,1,50)
print(x)
print('the type of x is:',type(x))
print(y)
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
plt.savefig("picture_1")
