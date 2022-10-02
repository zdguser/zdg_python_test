
#练习63 平均

# _num = float(input("please input a number (0 to quit): "))
# if int(_num) == 0:
#     print("wrong message.")
# else:
#     _add = 0
#     _n = 0
#     while int(_num) != 0:
#         _add = _add + _num
#         _n = _n + 1
#         _num = float(input("please input a number (0 to quit): "))
#     _ave = _add / _n
#     print("the average of the input numbers is:  %.2f " % _ave)

#练习64 折扣表

# n = int(input("please input the number: "))
# for i in range(n):
#     _num = float(input("please input the price: "))
#     _percent = float(input("please input the percent: "))
#     _former_price = _num / _percent
#     _discount = _former_price - _num
#     print("the former price is: %.2f " % _former_price, "the price is: %.2f " %  _num,"the discount is: %.2f " % _discount)

#练习65 温度换算表
# _list = range(0,101,10)
# _T = []
# print(len(_list))
# print(len(_T))
# print(_list)
# for i in _list:
#     _n = i * (9 / 5) + 32
#     _T.append(_n)
# print(_T)

#练习66 不要再花钱了


# 练习67 计算多边形的周长
# _x = input("please input: ")
# _y = input("please input: ")
# if (_x == ' ') or (_y == ' '):
#     print("end")
# else:
#     _l = 0
#     while _x != ' ':
#         _l = _l + (float(_x) ** 2 + float(_y) ** 2) ** 0.5
#         _x = input("please input: ")
#         _y = input("please input: ")
#     print(_l)

#练习68 计算平均绩点
# _num = input("please input： ")
# if _num == ' ':
#     print("wrong message")
# else:
#     _n,_sum,score= 0,0,0
#     while _num != ' ':
#
#         if _num == 'A+':
#             score = 4.0
#         elif _num == 'A':
#             score = 4.0
#         elif _num == 'A-':
#             score = 3.7
#         elif _num == 'B+':
#             score = 3.3
#         elif _num == 'B':
#             score = 3.0
#         elif _num == 'B-':
#             score = 2.7
#         elif _num == 'C+':
#             score = 2.3
#         elif _num == 'C':
#             score = 2.0
#         elif _num == 'C-':
#             score = 1.7
#         elif _num == 'D':
#             score = 1.0
#         elif _num == 'F':
#             score = 0.0
#         _sum = _sum + score
#         _n = _n + 1
#         _num = input("please input: ")
#
#     ave = _sum / _n
#     print(_sum)
#     print(_n)
#     print(ave)

#练习69 票价
# _num = input("please input: ")
# if _num == ' ':
#     print("wrong message")
# else:
#
#     _sum1,_sum2,_sum3,_sum4,_ticket,_n1,_n2,_n3,_n4 = 0,0,0,0,0,0,0,0,0
#     while _num != ' ':
#         _list = int(_num)
#         if _list <= 2:
#             _ticket = 0.00
#             _n1 += 1
#         elif (_list >= 3) and (_list <= 12):
#             _ticket = 14.00
#             _n2 += 1
#         elif _list > 65:
#             _ticket = 18.00
#             _n3 += 1
#         elif (_list >= 13) and (_list <= 65):
#             _ticket = 23.00
#             _n4 += 1
#         _sum1 = _n1 * 0
#         _sum2 = _n2 * 14.00
#         _sum3 = _n3 * 18.00
#         _sum4 = _n4 * 23.00
#         _num = input("please input: ")
#     print("小于2岁的有： %.d 人， 该组票费：%.2f 元" % (_n1,_sum1))
#     print("3到12岁的有： %.d 人， 该组票费：%.2f 元" % (_n2, _sum2))
#     print("大于65岁的有： %.d 人， 该组票费：%.2f 元" % (_n3, _sum3))
#     print("13到64岁的有： %.d 人， 该组票费：%.2f 元" % (_n4, _sum4))

#练习70 奇偶校验位
# _num = input("please input 8 number: ")
# if int(len(_num)) != 8:
#     print("wrong message")
# elif int(len(_num)) == 8:
#     _n1,_n2 = 0,0
#     for i in range(8):
#        if _num[i] == 1:
#            _n1 += 1
#        else:
#            _n2 += 1
#     _a = 0
#     if _n1 % 1 == 0:
#        _a = 0
#     elif _n1 % 1 == 1:
#        _a = 1
#     print("奇偶校验位是：  ")
#     print(_a)

#练习71 近似π
# _pi = 3
# print("第1个π值近似数: ",_pi)
# for i in range(1,15):
#     _pi = _pi + ((-1) ** (i+1)) * (4 / ((2 * i) * (2 * i + 1) * (2 * i + 2)))
#     print("第 %.d 个π值近似数: %.6f" % (i,_pi))

#练习72 Fizz-Buzz

# for i in range(1,101):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     if (i % 3 == 0) and (i % 5 == 0):
#         print("fizz and buzz")
#     else:
#         print(i)

#练习73 凯撒密码
#
# _data = list(input("please input some data: "))
# _num = int(input("please input the number of movement: "))
# _letter1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# _letter2 = 'abcdefghijklmnopqrstuvwxyz'
# _letter_1 = list(_letter1)
# _letter_2 = list(_letter2)
# _NEW = []
# for i in range(len(_data)):
#     for j in range(23,26,1):
#         if _data[i] == _letter_1[j]:
#            _data[i] = _letter_1[_num - (26 - j)]
#            _NEW.append(_data[i])
#     for k in range(23):
#         if _data[i] == _letter_1[k]:
#            _NEW.append(_letter_1[k + _num])
#
#     for m in range(23,26,1):
#         if _data[i] == _letter_2[m]:
#            _data[i] = _letter_2[_num - (26 - m)]
#            _NEW.append(_data[m])
#     for n in range(23):
#         if _data[i] == _letter_2[n]:
#            _NEW.append(_letter_2[n + _num])
# _str = ''.join(_NEW)
# print(_str)

#练习74 平方根
# _x = float(input("please input a number: "))
# _a = 1.0
# _guess = _x / 2
# while _a > 1e-12:
#     _guess = (_guess + (_x / _guess)) / 2
#     _a = abs(_guess * _guess - _x)
#     print("当前的近似值： %.8f" % _guess)
#
# print("最终的近似值： %.8f" % _guess)

#练习75 字符串是回文吗
# import math
# _str = list(input("please input a string: "))
# _n = len(_str)
# _a = math.floor(_n / 2)
# _b = 0
# for i in range(_a):
#     if _str[i] == _str[_n - i - 1]:
#        _b += 1
# if _b == _a:
#     print("this is a palindrome.")
# else:
#     print("this is not a palindrome.")

#练习76 多个单词的回文
# import math
# _str = list(input("please input a string: "))
# _n = len(_str)
# _a = math.floor(_n / 2)
# _b = 0
# for i in range(_a):
#     if _str[i] == _str[_n - i - 1]:
#        _b += 1
# if _b == _a:
#     print("this is a palindrome.")
# else:
#     print("this is not a palindrome.")

#练习77 乘法表

# for i in range(11):
#     if i == 0:
#        print("    ", end="")
#     else:
#        print("%4d" % i,end="")
# print("\n")
# for j in range(1,11):
#     print("%4d" % j, end="")
#     _n = 0
#     for k in range(1,11):
#        _n = j * k
#        print("%4d" % _n, end="")
#     print("\n")

#练习78 科拉茨猜想


#练习79 最大公约数
# _m = int(input("please input a number: "))
# _n = int(input("please input a number: "))
# _d = min(_m,_n)
# while (_m % _d != 0) or (_n % _d != 0):
#     _d -= 1
# print("这两个整数的最大公约数是： %.d" % _d)

#练习80 素因子
# _factor = 2
# _n = int(input("please input a int number: "))
# if _n < 2:
#     print("wrong message")
# else:
#     print("the prime factors of %d is: " % _n)
#     while _factor <= _n:
#         if int(_n % _factor) == 0:
#            print(_factor)
#            _n = _n / _factor
#         else:
#             _factor += 1

#练习81 二进制转换为十进制
# _num_2 = list(input("请输入二进制数字： "))
# _len = len(_num_2)
# _sum,_n = 0,0
# for i in range(_len):
#     if int(_num_2[i]) == 1:
#         _n = 1 * 2 ** (_len - i - 1)
#     elif int(_num_2[i]) == 0:
#         _n = 0
#     _sum += _n
# print("输出的10进制数为: %2d" % _sum)

#练习82 十进制转换到二进制
# import math
# _result = ''
# _q = int(input("请输入一个10进制的数： "))
# _n = 0
# while (_q >= 2) or (_q != 0):
#     _n = _q % 2
#     _result = str(_n) + _result
#     _q = math.floor(_q / 2)
# print(_result)

##练习83 最大整数
import random
_n = 0
_m = 0
while _n <= 3:
    _num = random.random()
    if _num > 0.5:
        print("T ",end='')
        _n += 1
    elif _num < 0.5:
        print("F ",end='')

print("    %d flips" % _n)











