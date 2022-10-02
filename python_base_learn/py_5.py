#练习110 排序
# alist = []
# _get = input("please input: ")
# while _get != '0':
#       alist.append(_get)
#       _get = input("please input: ")
# alist.sort()
# print(alist)

#练习111 倒序
# alist = []
# _get = input("please input: ")
# while _get != '0':
#       alist.append(_get)
#       _get = input("please input: ")
# alist.reverse()
# print(alist)

#练习112 删除异常值
# def _get_list():
#     alist = []
#     _get = input("please input: ")
#     while _get != '0':
#          alist.append(_get)
#          _get = input("please input: ")
#     return alist
# def main():
#     _list = _get_list()
#     _list.sort()
#     print('the initial list is:',_list)
#
#     _n = int(input("please input a positive number: "))
#     for i in range(_n):
#           _list.pop(i)
#     print(_list)
#     _l = len(_list)
#     for j in range(_n):
#           _list.pop(_l-1-j)
#     print('the new list is: ',_list)
# main()

#练习113 避免重复
# def _get_list():
#     alist = []
#     _get = input("please input: ")
#     while _get != ' ':
#          alist.append(_get)
#          _get = input("please input: ")
#     return alist
# def main():
#       _list = _get_list()
#       print('the initial list is: ',_list)
#       for i in _list:
#             _a = i
#             _n = 0
#             for j in _list:
#                   if i == j:
#                         _n += 1
#             if _n > 1:
#                   _list.remove(i)
#       print('the new list is: ',_list)
# main()

#练习114 负数、零和正数
# def _get_list():
#     alist = []
#     _get = input("please input: ")
#     while _get != ' ':
#          alist.append(_get)
#          _get = input("please input: ")
#     return alist
# def main():
#       _list = _get_list()
#       _list1 = []
#       _list2 = []
#       _list3 = []
#       for i in _list:
#             if int(i) > 0:
#                   _list1.append(i)
#             elif int(i) == 0:
#                   _list2.append(i)
#             elif int(i) < 0:
#                   _list3.append(i)
#       _list3.reverse()
#       _list1.reverse()
#
#       for j in _list3:
#             print(j)
#       for k in _list2:
#             print(k)
#       for l in _list1:
#             print(l)
# main()

#练习115 正因数表
# def _num_list(_n):
#       _a = 0
#       _list = []
#       for i in range(1,int(_n)):
#             if int(_n) % i == 0:
#                   _list.append(i)
#       return _list
# def main():
#       _num = int(input("please input a integer: "))
#       _list = _num_list(_num)
#       print("所有的公因子为：",_list)
# main()




