from pylab import *
import numpy as np
import matplotlib.pyplot as plt

file = '/home/qc2109/ZDG/draw/cases_XCdCl.dat'
orgfile = '/home/qc2109/ZDG/draw/org_v2'
f = open(file,'r')
org = open(orgfile,'r')

line = []
line = org.readlines()
line = line[0].strip('\n')
line = line.split(',')

xname = ['b1','b2','b3','b4','b5','b6']
yname = ['Cd-pressure-ALL','Cd-pressure-HEAD-UP','Cd-pressure-HEAD-NOSE','Cd-pressure-HEAD-DOWN','Cd-pressure-HEAD-REST',
'Cd-pressure-MIDDLE','Cd-pressure-TAIL-UP','Cd-pressure-TAIL-NOSE','Cd-pressure-TAIL-DOWN','Cd-pressure-TAIL-REST',
'Cd-Shear-ALL','Cd-Shear-HEAD-UP','Cd-Shear-HEAD-NOSE','Cd-Shear-HEAD-DOWN','Cd-Shear-HEAD-REST','Cd-Shear-MIDDLE',
'Cd-Shear-TAIL-UP','Cd-Shear-TAIL-NOSE','Cd-Shear-TAIL-DOWN','Cd-Shear-TAIL-REST',
'Cd-Total','Cl-Tail',]


n = int(input('please input the number of point: (int number)'))
nlist = []
for i in range(n):
    a = f.readline()
    nlist.append(a)

xlist1,xlist2= [],[]
for j in range(1,7):
    alist,blist = [],[]
    for jj in range(12):
        flist = nlist[jj].strip('\n')
        flist = flist.split(',')
        #flist = float(flist.split(','))
        alist.append(float(flist[j]))
    xlist1.append(alist)
    for kk in range(12,24):
        glist = nlist[kk].strip('\n')
        glist = glist.split(',')
        #glist = float(glist.split(','))
        blist.append(float(glist[j]))
    xlist2.append(blist)
#print(xlist1)
#print(xlist2)
#print(xlist1[0])

orglist,optlist = [],[]
for k in range(7,29):
    clist,dlist = [],[]
    for jj in range(12):
        flist = nlist[jj].strip('\n')
        flist = flist.split(',')
        #flist = float(flist.split(','))
        clist.append(float(flist[k]))
    orglist.append(clist)
    for kk in range(12,24):
        glist = nlist[kk].strip('\n')
        glist = glist.split(',')
        #glist = float(glist.split(','))
        dlist.append(float(glist[k]))
    optlist.append(dlist)

#print(orglist[20])
#print(optlist[20])


iter = 0
dt = ['A','B','C','D','E','F']
for xx in range(6):
    get_xlist1 = np.array(xlist1[xx])
    get_xlist2 = np.array(xlist2[xx])
    
    for yy in range(22):

        get_orglist = np.array(orglist[yy])
        get_optlist = np.array(optlist[yy])

        fig = figure()
        figure(figsize=(10,6),dpi=80)
        scatter(get_xlist1,get_orglist,color='blue',label='Initial')
        scatter(get_xlist2,get_optlist,color='red',label='Optimal soluion')
        legend(loc='upper right')

        m = float(line[yy+7])
        plot([-1,1],[m,m],color='black')

        str1 = xname[xx]
        str2 = yname[yy]
        xlabel(str1)
        ylabel(str2)

        # iter = (xx + 1) * (yy + 1)
        # iter = str(iter)
        # dd = str(dt[xx])
        str3 = 'fig' + '_' + str2 + '_' + str1 + '.png'
        savefig(str3)

f.close()
org.close()



    








