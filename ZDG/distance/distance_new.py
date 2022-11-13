import numpy as np
import math

###读取每行数据，记录每行数据到一个列表，每行即代表一个点的位置
f = open('point_location','r')
chart = open('point_chart_distance','w')
chart.write('the distance of point is:' + '\n')


###按行读取文件的每行数据，写入列表
getlist = []
d= int(input('please input the dim of data:(int number)'))
for i in range(d):
    a = f.readline()
    getlist.append(a)


n = len(getlist)
getdistance = []
l = 0

#####输出数据文件表头
str1 = ' '*10
for i in range(n):
    str1 += 'x' + str(i) + ' ' * 8
#str1 = ' '*10+'x0'+' '*8+'x1'+' '*8+'x2'+' '*8+'x3'+' '*8+'x4'+' '*8+'x5'+' '*8
chart.write(str1 +'\n')

###计算任意两点之间的距离
for j in range(n-1):
    alist = getlist[j].strip('\n')
    alist = alist.split(',')
    
    ###调整写出文件到整齐性，每个数字占6格，相邻两个数字之间的空格为一个tab(4格),总占据为10格
    chart.write('x'+str(j)+' '*8)
    chart.write(' '*10)
    chart.write(' '*l)

    for k in range(j+1,n):
          blist = getlist[k].strip('\n')
          blist = blist.split(',')
          
          m = len(blist)
          
          sum,dis = 0.0,0.0
          for index in range(m):
            vv = math.pow(float(alist[index]) - float(blist[index]),2)
            sum += vv 
          dis = round(math.pow(sum,0.5),4)
          dis = str(dis)
          
          ###计算distance的长度，方便文件在写入数据时补齐distance约去的0
          N = 6 - len(dis)
          chart.write(dis + ' '*N + '    ')        

          getdistance.append(dis)
    
    ###保证写入数据的整齐     
    chart.write('\n')
    l += 10

    ####输出最后一个参数
    while j == n - 2:
        chart.write('x'+str(j+1))
        break
   



#res.write('the distance of j point to k point is: {}'.format(sum ** 0.5))
print('the distance is :', getdistance)

f.close()
chart.close()