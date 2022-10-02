

####文件到打开与运用
# fname = input("please input the name of file:")
# inf = open(fname,"r")

##按行读取数据，一个数据占据一行
# total = 0

# line = inf.readlines() #字符串组,readline()一次读取一行，read一次读取全部数据，readlines也是读取全部数据
#去除行末符号
#line = line.rstrip()
# print(line)

# while line != "":

# for i in range(10):
#     total = total + float(line[i])

# inf.close()

# print("the total is: %.2f" % total)


###################################################################

fname1 = input("please input the filename:")
fname2 = input("please input the filename:") 

inf1 = open(fname1,"r")
inf2 = open(fname2,"w")

line1 = inf1.readlines()


# for i in range(len(line2)):
for i in line1:
    
    inf2.write(str(i))

print(line1)

inf1.close()
inf2.close()










