

#练习85 计算斜边
# def square(_a,_b):
#     _c = (_a ** 2 + _b ** 2) ** 0.5
#     return _c
# def main():
#     a = float(input("please input a number: "))
#     b = float(input("please input a number: "))
#     c = square(a,b)
#     print("直角三角形斜边长为：%.2f " % c)
# main()

#练习86 出租车费
# def square(_s):
#     _cost = ((_s * 1000) / 140) * 0.25 + 4.00
#     return _cost
# def main():
#     _a = float(input("please input the distance: "))
#     _c = square(_a)
#     print("车费为：%.2f " % _c)
# main()

#练习87 运费计算器
# def square(_n):
#     _cost = 10.95 + 2.95 * (_n - 1)
#     return _cost
# def main():
#     _a = float(input("please input the number: "))
#     _c = square(_a)
#     print("邮费为：%.2f " % _c)
# main()

#练习88
# def square(_a,_b,_c):
#     _list = []
#     _list.append(_a)
#     _list.append(_b)
#     _list.append(_c)
#     _list.sort()
#     _cost = float(_list[1])
#     return _cost
# def main():
#     _a = float(input("please input the number: "))
#     _b = float(input("please input the number: "))
#     _c = float(input("please input the number: "))
#     _d = square(_a,_b,_c)
#     print("三个数的中值为：%.2f " % _d)
# main()

#test 调用其他文件里的函数 if __name__ == "__main__":
# from test1 import square
# def main():
#     _a = float(input("please input the number: "))
#     _b = float(input("please input the number: "))
#     _c = float(input("please input the number: "))
#     _d = square(_a,_b,_c)
#     print("三个数的中值为：%.2f " % _d)
# main()

#练习89 将整数转换为序数
# def number(n):
#     if n == 1:
#         print("序数为： 第一")
#     elif n == 2:
#         print("序数为： 第二")
#     elif n == 3:
#         print("序数为： 第三")
#     elif n == 4:
#         print("序数为： 第四")
#     elif n == 5:
#         print("序数为： 第五")
#     elif n == 6:
#         print("序数为： 第六")
#     elif n == 7:
#         print("序数为： 第七")
#     elif n == 8:
#         print("序数为： 第八")
#     elif n == 9:
#         print("序数为： 第九")
#     elif n == 10:
#         print("序数为： 第十")
#     elif n == 11:
#         print("序数为： 第十一")
#     elif n == 12:
#         print("序数为： 第十二")
#     else:
#         print(" ")
# def main():
#     _n = int(input("please input a number: "))
#     number(_n)
# main()

#练习90 圣诞节的12天
# def number(n):
#     if n == 1:
#         print("On the first day of Christmas")
#     elif n == 2:
#         print("my true love sent to me:")
#     elif n == 3:
#         print("A partridge in a pear tree.")
#         print("                           ")
#     elif n == 4:
#         print("On the second day of Christmas")
#     elif n == 5:
#         print("my true love sent to me:")
#     elif n == 6:
#         print("Two turtle doves,")
#     elif n == 7:
#         print("And a partridge in a pear tree.")
#         print("                           ")
#     elif n == 8:
#         print("On the third day of Christmas")
#     elif n == 9:
#         print("my true love sent to me:")
#     elif n == 10:
#         print("Three French hens,")
#     elif n == 11:
#         print("Two turtle doves,")
#     elif n == 12:
#         print("And a partridge in a pear tree.")
#     else:
#         print(" ")
# def main():
#     _n1 = int(input("please input a number: "))
#     number(_n1)
#     _n2 = int(input("please input a number: "))
#     number(_n2)
#     _n3 = int(input("please input a number: "))
#     number(_n3)
#     _n4 = int(input("please input a number: "))
#     number(_n4)
#     _n5 = int(input("please input a number: "))
#     number(_n5)
#     _n6 = int(input("please input a number: "))
#     number(_n6)
#     _n7 = int(input("please input a number: "))
#     number(_n7)
#     _n8 = int(input("please input a number: "))
#     number(_n8)
#     _n9 = int(input("please input a number: "))
#     number(_n9)
#     _n10 = int(input("please input a number: "))
#     number(_n10)
#     _n11 = int(input("please input a number: "))
#     number(_n11)
#     _n12 = int(input("please input a number: "))
#     number(_n12)
# main()

#练习91 从公历日期到序数日期
#判断是否是闰年
# def _num_year(_year):
#     _a = 0
#     if int(_year) % 400 == 0:
#         _a = 366
#     elif int(_year) % 100 == 0:
#         _a = 365
#     elif int(_year) % 4 == 0:
#         _a = 366
#     else:
#         _a = 365
#     return _a
# def _date_second(_date_year):
#     if _date_year == 365:
#        _b =28
#     elif _date_year == 366:
#        _b = 29
#     return _b
#
# def ordinalDate(_day,_month,_year):
# #判断是否是闰年
#     _date_year = _num_year(_year)
#     _b = _date_second(_date_year)
#
#     _date_month = int(_month)
#     if int(_month) == 1:
#        _count_day = _day
#     elif int(_month) == 2:
#        _count_day = 31 + _day
#     elif int(_month) == 3:
#        _count_day = 31 + _b + _day
#     elif int(_month) == 4:
#        _count_day = 31 * 2 + _b + _day
#     elif int(_month) == 5:
#        _count_day = 31 * 2 + _b + 30 + _day
#     elif int(_month) == 6:
#        _count_day = 31 * 3 + _b + 30 + _day
#     elif int(_month) == 7:
#        _count_day = 31 * 3 + _b + 30 * 2 + _day
#     elif int(_month) == 8:
#        _count_day = 31 * 4 + _b + 30 * 2 + _day
#     elif int(_month) == 9:
#        _count_day = 31 * 5 + _b + 30 * 2 + _day
#     elif int(_month) == 10:
#        _count_day = 31 * 5 + _b + 30 * 3 + _day
#     elif int(_month) == 11:
#        _count_day = 31 * 6 + _b + 30 * 3 + _day
#     elif int(_month) == 12:
#        _count_day = 31 * 6 + _b + 30 * 4 + _day
#     return _count_day
# def main():
#     _day = int(input("please input a number: "))
#     _month = int(input("please input a number: "))
#     _year = int(input("please input a number: "))
#
#     _num = ordinalDate(_day,_month,_year)
#     print("序数日期是： %.d " % _num)
#
# main()

#练习92 从序数日期到公历日期
# def _num_year(_year):
#     _a = 0
#     if int(_year) % 400 == 0:
#         _a = 366
#     elif int(_year) % 100 == 0:
#         _a = 365
#     elif int(_year) % 4 == 0:
#         _a = 366
#     else:
#         _a = 365
#     return _a
# def _date_second(_date_year):
#     _b = 0
#     if _date_year == 365:
#        _b =28
#     elif _date_year == 366:
#        _b = 29
#     return _b

# def ordinalDate(_num,_year):
#     _date_year = _num_year(_year)
#     _b = _date_second(_date_year)
#     _n_month = 0
#     _n_day = 0
#
#     if (int(_num) >= 1) and (int(_num) <= 31):
#        _n_month = 1
#        _n_day = int(_num)
#     elif (int(_num) > 31) and (int(_num) <= (31 + int(_b))):
#         _n_month = 2
#         _n_day = int(_num) - 31
#     elif (int(_num) > (31 + int(_b))) and (int(_num) <= (31 * 2 + int(_b))):
#         _n_month = 3
#         _n_day = int(_num) - 31 - int(_b)
#     elif (int(_num) > (31 * 2 + int(_b))) and (int(_num) <= (31 * 2 + 30 + int(_b))):
#         _n_month = 4
#         _n_day = int(_num) - 31 * 2 - int(_b)
#     elif (int(_num) > (31 * 2 + 30 + int(_b))) and (int(_num) <= (31 * 3 + 30 + int(_b))):
#         _n_month = 5
#         _n_day = int(_num) - 31 * 2 - 30 - int(_b)
#     elif (int(_num) > (31 * 3 + 30 + int(_b))) and (int(_num) <= (31 * 3 + 30 * 2 + int(_b))):
#         _n_month = 6
#         _n_day = int(_num) - 31 * 3 - 30 - int(_b)
#     elif (int(_num) > (31 * 3 + 30 * 2 + int(_b))) and (int(_num) <= (31 * 4 + 30 * 2 + int(_b))):
#         _n_month = 7
#         _n_day = int(_num) - 31 * 3 - 30 * 2 - int(_b)
#     elif (int(_num) > (31 * 4 + 30 * 2 + int(_b))) and (int(_num) <= (31 * 5 + 30 * 2 + int(_b))):
#         _n_month = 8
#         _n_day = int(_num) - 31 * 4 - 30 * 2 - int(_b)
#     elif (int(_num) > (31 * 5 + 30 * 2 + int(_b))) and (int(_num) <= (31 * 5 + 30 * 3 + int(_b))):
#         _n_month = 9
#         _n_day = int(_num) - 31 * 5 - 30 * 2 - int(_b)
#     elif (int(_num) > (31 * 5 + 30 * 3 + int(_b))) and (int(_num) <= (31 * 6 + 30 * 3 + int(_b))):
#         _n_month = 10
#         _n_day = int(_num) - 31 * 5 - 30 * 3 - int(_b)
#     elif (int(_num) > (31 * 6 + 30 * 3 + int(_b))) and (int(_num) <= (31 * 6 + 30 * 4 + int(_b))):
#         _n_month = 11
#         _n_day = int(_num) - 31 * 6 - 30 * 3 - int(_b)
#     elif (int(_num) > (31 * 6 + 30 * 4 + int(_b))) and (int(_num) <= (31 * 7 + 30 * 4 + int(_b))):
#         _n_month = 12
#         _n_day = int(_num) - 31 * 6 - 30 * 4 - int(_b)
#
#     return _n_month,_n_day
#
#
# def main():
#     _num = int(input("please input a number: "))
#     _year = int(input("please input a number: "))
#     _another_num = int(input("please input a number: "))
#     _get_month,_get_day = ordinalDate(_num,_year)
#     _get_month_1, _get_day_1 = ordinalDate(int(_num + _another_num), _year)
#     print("对应日期为： %.d 月  %.d 日" % (_get_month,_get_day))
#     print("该天%.d 天后对应日期为： %.d 月  %.d 日" % (_another_num,_get_month_1, _get_day_1))
# main()

#练习93 在终端端口中居中一个显示字符串
# def _middle(_s,_w):
#     _n = 0
#     _a = ' '
#     if len(_s) > int(_w):
#         return _s
#     elif len(_s) <= int(_w):
#         _n = int((len(_s) - int(_w)) / 2)
#         _str1 = _a * _n
#         return _str1,_s
# def main():
#     _s = input("please input something: ")
#     _w = int(input("please input the width of string: "))
#     _str,_l = _middle(_s,_w)
#     print(_l,_str)
# main()

#练习94 它是一个有效的三角形吗
# def _triangle(_a,_b,_c):
#     _n = 1
#     if (_a >= (_b + _c)) and (_b >= (_a + _c)) and (_c >= (_b + _a)):
#         _n = 0
#     else:
#         _n = 1
#     return _n
# def main():
#     a = int(input("please input a number: "))
#     b = int(input("please input a number: "))
#     c = int(input("please input a number: "))
#     _num = _triangle(a,b,c)
#     if _num == 1:
#         print("可以构成三角形")
#     elif _num == 0:
#         print("这不可以构成三角形")
# main()

#练习95 大写


#练习96 字符串是否表示整数
#
# def isInteger(_str):
#
#    _str = _str.strip()
#    if (_str[0] == '+' or _str[0] == '-') and s[1:].isdigit():
#        return True
#    if _str.isdigit():
#        return True
#    return False
#
# def main():
#     _s = input("please input a string: ")
#     if isInteger(_s):
#         print("the string is a integer ")
#     else:
#         print("the string is a integer ")
# main()

#练习97 操作符的优先级
# def priority(_str):
#     if (_str == '+') or (_str == '-'):
#         result = 1
#     elif (_str == '*') or (_str == '/'):
#         result = 2
#     elif _str == '^':
#         result = 3
#     else:
#         result = -1
#     return result
#
# def main():
#     _str = input("please input a string: ")
#     _n = int(priority(_str))
#     print("这个操作符的等级是：%d" % _n)
# main()

#练习98 一个数是素数吗
# def _Prime_number(_num):
#     if _num == 1:
#         return False
#     if _num == 2:
#         return True
#     _b = 0
#
#     for i in range(2,_num):
#         _a = _num % i
#         if _a == 0:
#             _b += 1
#     if _b == 0:
#         return True
#     return False
#
# def main():
#     _s = int(input("please input a number: "))
#     if _Prime_number(_s):
#         print("this is  a prime number")
#     else:
#         print("this is not a prime number")
# main()

#练习99 下一个素数
# def _Prime_number(_num):
#     if _num == 1:
#         return False
#     if _num == 2:
#         return True
#     _b = 0
#     for i in range(2,_num):
#         _a = _num % i
#         if _a == 0:
#             _b += 1
#     if _b == 0:
#         return True
#     return False
# def nextPrime(_num):
#     _num += 1
#     while not(_Prime_number(_num)):
#         _num += 1
#     return _num
# def main():
#     _s = int(input("please input a number: "))
#     _c = nextPrime(_s)
#     print("the next prime number is : %d" % _c)
# main()

# 练习100 随机密码
# import random
# def password():
#     _a = random.randint(7,10)
#     _pw = ''
#     for i in range(_a):
#         _c = random.randint(33,126)
#         _pw += chr(_c)
#     return _pw
# def main():
#     _get_pd = password()
#     print(_get_pd)
# main()

#练习101 随机车牌
# import random
# def _car_number():
#     _a = random.random()
#     _n = 0
#     if _a >= 0.5:
#         _n = 6
#     else :
#         _n = 7
#     _pw = ''
#     for i in range(_n):
#         _b = random.random()
#         if _b >= 0.5:
#             _c = random.randint(65,90)
#         else:
#             _c = random.randint(48,57)
#         _pw += chr(_c)
#     return _pw
# def main():
#     _get_pw = _car_number()
#     print(_get_pw)
# main()

#练习102 检查密码

#
# def _true_password(_pw):
#     _l = len(_pw)
#
#     if _l >= 8:
#         _a,_b,_c = 0,0,0
#         for i in range(_l):
#            if _pw[i].isdigit():
#                _a += 1
#            if _pw[i].isupper():
#                _b += 1
#            if _pw[i].islower():
#                _c += 1
#         if (_a > 0) and (_b > 0) and (_c > 0):
#             return True
#         else:
#             return False
#     else:
#         return False
# def main():
#     _str = input("please input a string: ")
#     if _true_password(_str):
#         print("correct password")
#     else:
#         print("wrong password")
# main()

#练习103 随机的好密码
# import random
# def password():
#     _a = random.randint(7,10)
#     _pw = ''
#     for i in range(_a):
#         _c = random.randint(33,126)
#         _pw += chr(_c)
#     return _pw
# def _true_password(_pw):
#     _l = len(_pw)
#
#     if _l >= 8:
#         _a,_b,_c = 0,0,0
#         for i in range(_l):
#            if _pw[i].isdigit():
#                _a += 1
#            if _pw[i].isupper():
#                _b += 1
#            if _pw[i].islower():
#                _c += 1
#         if (_a > 0) and (_b > 0) and (_c > 0):
#             return True
#         else:
#             return False
#     else:
#         return False
# def main():
#     _str = password()
#     print(_str)
#     if _true_password(_str):
#         print("correct password")
#     else:
#         print("wrong password")
# main()

#练习104 十六进制和十进制数字

#练习105 任意进制之间的转换

#练习106 一个月的天数
# def _year_count(_year):
#     if int(_year) % 400 == 0:
#         return True
#     elif int(_year) % 100 == 0:
#         return False
#     elif int(_year) % 4 == 0:
#         return True
#     else:
#         return False
#
# def _day_of_month(_year,_month):
#     if _year_count(_year):
#         _feb = 29
#     else:
#         _feb = 28
#     for i in range(1,13):
#         if (int(_month) == 1) or (int(_month) == 3) or (int(_month) == 5) or (int(_month) == 7) or (int(_month) == 8) or (int(_month) == 10) or (int(_month) == 12):
#             _day = 31
#         elif (int(_month) == 4) or (int(_month) == 6) or (int(_month) == 9) or (int(_month) == 11):
#             _day = 30
#         elif int(_month) == 2:
#             _day = _feb
#     return _day
#
# def main():
#     _month = int(input("please input the month: "))
#     _year = int(input("please input the year: "))
#     _get_day = _day_of_month(_year,_month)
#     print("这个月的天数为：%d" % _get_day)
# main()

#练习107 最简分数
# def _common_factor(_a,_b):
#     _n = min(_a,_b)
#     while not((_a % _n == 0) and (_b % _n == 0)):
#         _n -= 1
#     return _n
# def _Simplification(_num1,_num2):
#     _get = _common_factor(_num1,_num2)
#     _num3 = _num1 / _get
#     _num4 = _num2 / _get
#     return _num3,_num4
# def main():
#     _get_num1 = int(input("please input the molecular: "))
#     _get_num2 = int(input("please input the denominator: "))
#     _new_num1,_new_num2 = _Simplification(_get_num1,_get_num2)
#     print("the new molecular is: %d" % _new_num1)
#     print("the new denominator is: %d" % _new_num2)
# main()

#练习108 减少度量单位


#练习109 神奇的日子
# def amazing_day(_day,_month,_year):
#     _a = int(_year[2]) * 10 + int(_year[3])
#     _b = int(_day) * int(_month)
#     if _a == _b:
#         return True
#     else:
#         return False
# def main():
#     _day = input("please input the day: ")
#     _month = input("please input the month: ")
#     _year = input("please input the year: ")
#     if amazing_day(_day,_month,_year):
#         print("that is a amazing day")
#     else:
#         print("that is not a amazing day")
# main()
