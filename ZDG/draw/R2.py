import math
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

####v2的数据
Cdval = [0.136115,0.135844,0.135378,0.135422,0.135179,0.135728]
Cdpre = [0.135419,0.135221,0.131999,0.133007,0.129889,0.133461]

####v21的数据
# Cdval = [0.133015,0.132989,0.133089,0.132844,0.132959,0.133693,
# 0.134202,0.134023,0.133439,0.134747,0.134666,0.134373]
# Cdpre = [0.132879,0.132578,0.131455,0.132284,0.132369,0.100614,
# 0.117437,0.118486,0.125533,0.122162,0.121019,0.126869]

###数学期望函数
def avg(list):
    m = len(list)
    sum = 0.0
    for i in range(m):
        sum += float(list[i]) 
    a = sum /m
    return a
###方差函数
def variance(list):
    m = len(list)
    sum,sum1 = 0.0,0.0
    for i in range(m):
        sum += float(list[i]) 
    a = sum /m

    for j in range(m):
        sum1 += (float(list[j]) - a ) ** 2
    b = sum1 / m
    return b

####拟合斜率公式
def slope(list1,list2):
    sum1,sum2 = 0.0,0.0
    m = len(list1)
    getlist1 = np.array(list1)
    getlist2 = np.array(list2)
    xx,xy = 0.0,0.0
    for i in range(m):
        xx += math.pow(getlist1[i],2)
        xy += getlist1[i] * getlist2[i]
    k = xy / xx
    return k

EX = avg(Cdval)
EY = avg(Cdpre)
DX = variance(Cdval)
DY = variance(Cdpre)

n = int(input('please input the number of data: (int number)'))
XYlist = []
N,sum = 0.0,0.0
for i in range(n):
    N = float(Cdval[i]) * float(Cdpre[i])
    XYlist.append(N)
    sum += N
EXY = sum / n
s1 = DX ** 0.5
s2 = DY ** 0.5

# print(EX)
# print(EY)
# print(DX)
# print(DY)

cov = EXY - EX * EY
R = cov / (s1 * s2)
print('协方差为： %.6f' % cov)
print('相关度为： %.6f' % R)

##########################################################
k = slope(Cdpre,Cdval)
print("slope is: %.4f" % k)
x = np.array(Cdpre)
y = k * x

##########################################################

getCdval = np.array(Cdval)
getCdpre = np.array(Cdpre)

fig = figure()
figure(figsize=(10,6),dpi=80)

plot(x,y,'r')

scatter(getCdpre,getCdval,color='blue',label='pre-opt')
legend(loc='upper right')
xlabel('pre-value')
ylabel('opt-value')

# ###设置横轴、纵轴的记号
# xticks(np.linspace(0.130,0.137,8,endpoint=True))
# ####设置横轴、纵轴的上下限
# xlim(0.130,0.137)

# yticks(np.linspace(0.132,0.140,9,endpoint=True))
# ylim(0.132,0.140)

# grid(True) #网格
# title('line-point')

savefig('pre-opt-v21')

