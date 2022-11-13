import numpy as np
import math

###读取每行数据，记录每行数据到一个列表，每行即代表一个点的位置
f = open('point_location','r')
res = open('point_distance','w')
table = open('point_table_distance','w')


res.write('the distance of is:' + '\n')
table.write('the distance of point is:' + '\n')


getlist = []
for i in range(6):
    a = f.readline()
    getlist.append(a)


# alist = getlist[0].split(',')
# print(alist)
# print(len(alist))
# print(type(alist))

###计算任意两点之间的距离
n = len(getlist)
getdistance = []
for j in range(n-1):
    alist = getlist[j].strip('\n')
    alist = alist.split(',')

    for k in range(j+1,n):
          blist = getlist[k].strip('\n')
          blist = blist.split(',')
          
          
          m = len(blist)
          
          sum = 0.0
          dis = 0.0
          for index in range(m):
            vv = math.pow(float(alist[index]) - float(blist[index]),2)
            sum += vv 
          dis = round(math.pow(sum,0.5),4)
          dis = str(dis)
          #print(len(dis))        

          getdistance.append(dis)
          res.write(dis + '\n')
          table.write(dis + '   ')
    table.write('\n')




          #res.write('the distance of j point to k point is: {}'.format(sum ** 0.5))
print('the distance is :', getdistance)

f.close()
res.close()
table.close()



