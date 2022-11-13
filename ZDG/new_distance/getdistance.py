import numpy as np
import math

file = '/home/qc2109/ZDG/point_location'
f = open(file,'r')
#f = open('point_location','r')

chart1 = open('/home/qc/ZDG/new/point_chart1_distance','w')
def distance():
    ###读取每行数据，记录每行数据到一个列表，每行即代表一个点的位置
    
    chart1.write('the distance of point is:' + '\n')

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
    chart1.write(str1 +'\n')

    ###计算任意两点之间的距离
    for j in range(n-1):
        alist = getlist[j].strip('\n')
        alist = alist.split(',')
    
    ###调整写出文件到整齐性，每个数字占6格，相邻两个数字之间的空格为一个tab(4格),总占据为10格
        chart1.write('x'+str(j)+' '*8)
        chart1.write(' '*10)
        chart1.write(' '*l)

        for k in range(j+1,n):
            blist = getlist[k].strip('\n')
            blist = blist.split(',')

            m = len(blist)
          
            sum,dis = 0.0,0.0
            for index in range(1,m):
                vv = math.pow(float(alist[index]) - float(blist[index]),2)
            sum += vv 
            dis = round(math.pow(sum,0.5),4)
            dis = str(dis)
          
            ###计算distance的长度，方便文件在写入数据时补齐distance约去的0
            N = 6 - len(dis)
            chart1.write(dis + ' '*N + '    ')

            getdistance.append(dis)
    
        ###保证写入数据的整齐     
        chart1.write('\n')
        l += 10
    
        ####输出最后一个参数
        while j == n - 2:
            chart1.write('x'+str(j+1))
            break
    
    f.close()
    chart1.close()

#distance()
