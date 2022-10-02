#练习136 反向查找
# con = {'apple':10,'banana':10,'melon':12}
# print(con.values['10'])

# def creat_dictionary(_n):
#     constants = {}
#     while len(constants) <= _n:
#         _str = input("please input a string: ")
#         if _str in constants:
#             constants[_str] += 1
#         else:
#             constants[_str] = 1
#     return constants
# def reverseLookup(_val,_dict):
#     for i in _dict:
#         if int(_val) == _dict[i]:
#            print("the keys of this value %d is: " % int(_val),i)
# def main():
#     _n = int(input("please input a integer number: "))
#     _dict = creat_dictionary(_n)
#     print(_dict)
#     _val = int(input("input a values: "))
#     reverseLookup(_val, _dict)
# main()

#练习137 两个骰子的模拟
# import random
# def main():
#     _dict = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
#     for i in range(1000):
#         _val1 = random.randint(1,6)
#         _val2 = random.randint(1,6)
#         _val = _val1 + _val2
#         for k in _dict:
#             if _val == int(k):
#                _dict[k] += 1
#     _list = []
#     _sum = 0
#     for j in _dict:
#         _list.append((_dict[j]/1000) * 100)
#         _sum += _dict[j]/1000
#     print(_sum)
#     print("Total Percent","    ","Simulated Percent","    ","Expected",end='')
#     print('\n')
#     _list1 = [2.78,5.56,8.33,11.11,13.89,16.67,13.89,11.11,8.33,5.56,2.78]
#     for x in range(11):
#         print("%6d" % (x+2),"               ","%.2f" % _list[x],"                ",_list1[x])
# main()

#练习138 发短信
# _dict = {'1':'.,?!:','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8 ':'TUV','9':'WXYZ','0':' ',}
# _str = input("please input a string: ")
# _list = []
# for i in _str:
#     for j in _dict:
#         _str1 = _dict[j]
#         for k in range(len(_str1)):
#             if i == _str1[k]:
#                 _list.append(j)
#                 if k != 0:
#                    _list.append(k+1)
#                 elif k == 0:
#                    _list.append(j)
# print(_list)

#莫尔斯电码
# _dict = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'- -.','H':'....','I':'..', \
#          'J':'.- - -','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.- -.','Q':'- -.-','R':'.-.', \
#          'S':'...','T':'-','U':'..-','V':'...-','W':'.- -','X':'-..-','Y':'-.- -','Z':'- -..','0':'- - - - -', \
#          '1':'.- - - -','2':'..- - -','3':'...- -','4':'....-','5':'.....','6':'-....','7':'- -...','8':'- - -..','9':'----.'}
# _str = input("please input a string: ")
# _list = []
# for i in _str:
#     for k in _dict:
#         if i == k:
#             _list.append(_dict[k])
#
# print(_list)

#练习140 邮政编码
# _dict = {'A':'纽芬兰','B':'新斯科舍','C':'爱德华王子岛','E':'新不伦瑞克','G':'魁北克','H':'魁北克','J':'魁北克',\
#          'K':'安大略省','L':'安大略省','M':'安大略省','N':'安大略省','P':'安大略省','R':'马尼托巴省','S':'萨斯客彻温省',\
#          'T':'阿尔伯特省','V':'不列颠哥伦比亚省','X':'努勒维特或西北地区','Y':'育空'}
# _str = list(input("please input a string: "))
# # _list = ['A','B','C','E','G','H','J','K','L','M','N','P','R','S','T','V','X','Y']
# _list1 = []
# for i in _dict:
#     if i == _str[0]:
#         _list1.append(_dict[i])
# if _str[1] == '0':
#     _list1.append('countryside')
# else:
#     _list1.append('city')
# print(_list1)

#练习141 用英语写数字


#练习142 独特的字符



#








