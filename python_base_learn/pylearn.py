import math
import time
#练习1 邮寄地址
#print("my name is zdg, and my email is 1643576849@qq.com")

#练习2 你好
# name = input("please input your name!")
# print ("hello %5s" % name)

#练习3 房间的面积
# length = float(input("please input the length in meter: "))
# width = float(input("please input the width in meter:"))
# area = length * width
# print("the area of the house is: %.2f square meter" % area)

#练习4 农场的面积
# length = float(input("please input the length in feet: "))
# width = float(input("please input the width in feet:"))
# area = length * width
# area_1 = area / 43560
# print("the area of the house is: %.2f acre" % area_1)

#练习5 瓶子押金
# small_bottle = int(input("please input the number of small bottle: "))
# big_bottle = int(input("please input the number of big bottle: "))
# money_of_bootle = small_bottle * 0.10 + big_bottle * 0.25
# print("the money of the bottle is: %.2f us dollar" % money_of_bootle)

#练习6 征税和小费
# cost_of_food = float(input("please input the cost of the food: "))
# tax_of_food = cost_of_food * 0.20
# tip_of_food = cost_of_food * 0.18
# total_cost = cost_of_food + tax_of_food + tip_of_food
# print("the tax of the food is: %.2f us dollar" % tax_of_food)
# print("the tip of the food is: %.2f us dollar" % tip_of_food)
# print("the total cost of the food is: %.2f us dollar" % total_cost)

#练习7 前n个正整数的和
# int_number = int(input("please input a int number: "))
# sum_number = (int_number * (int_number+1))/2
# print("the sum of the input number is: %.2f" %sum_number)

#练习8 widget和gizmo
# widget_number = int(input("please input the number of widget : "))
# gizmo_number = int(input("please input the number of gizmo : "))
# total_weight = widget_number * 75 + gizmo_number * 112
# print("the total weight in gram is: %.2f" % total_weight)

#练习9 复利
# save_of_money = float(input("please input the money of the save: "))
# first_year_money = save_of_money * (1 + 0.04)
# second_year_money = save_of_money * (1 + 0.04)**2
# three_year_money = save_of_money * (1 + 0.04)**3
# print("the first year money is: %.2f" % first_year_money,"the second year money is: %.2f" % second_year_money,"the three year money is: %.2f" % three_year_money)
# print("the first year money is: %.2f" % first_year_money)
# print("the second year money is: %.2f" % second_year_money)
# print("the three year money is: %.2f" % three_year_money)


#练习10 算术

# a = int(input("please input a int numbers: "))
# b = int(input("please input a int numbers: "))
# number_1 = a + b
# number_2 = a - b
# number_3 = a * b
# number_4 = a / b
# number_5 = a % b
# number_6 = math.log(a,10)
# number_7 = a ** b
# print("the number is: %.2f" % number_1)
# print("the number is: %.2f" % number_2)
# print("the number is: %.2f" % number_3)
# print("the number is: %.2f" % number_4)
# print("the number is: %.2f" % number_5)
# print("the number is: %.2f" % number_6)
# print("the number is: %.2f" % number_7)

#练习11 燃烧效率
# a = float(input("please input a MPG numbers: "))
# b = a * (3.785/(100*1.61))
# print("the number is: %.2f" % b)

#练习12 地球上两点之间的距离
# a_1 = float(input("请输入1点的经度值: "))
# b_1 = float(input("请输入1点的纬度值: "))
# a_2 = float(input("请输入2点的经度值: "))
# b_2 = float(input("请输入2点的纬度值: "))
# t_1 = math.radians(a_1)
# g_1 = math.radians(b_1)
# t_2 = math.radians(a_2)
# g_2 = math.radians(b_2)
# l = 6371.01 * math.acos(math.sin(t_1) * math.sin(t_2) + math.cos(t_1) * math.cos(t_2) * math.cos(g_1 - g_2))
# print("the distance of two points im kilometer is: %.2f" % l)

#练习13 找零钱
# cents_200 = 200
# cents_100 = 100
# cents_25 = 25
# cents_10 = 10
# cents_5 = 5
# cents_1 = 1
#
# cents = int(input("please input a int numbers: "))
#
# print(" ", cents // cents_200, "cents_200" )
# cents = cents % cents_200
# print(" ", cents // cents_100, "cents_100" )
# cents = cents % cents_100
# print(" ", cents // cents_25, "cents_25" )
# cents = cents % cents_25
# print(" ", cents // cents_10, "cents_10" )
# cents = cents % cents_10
# print(" ", cents // cents_5, "cents_5" )
# cents = cents % cents_5
# print(" ", cents, "cents_1" )

#练习14 身高单位
# feet = int(input("please input a feet  numbers: "))
# inch = int(input("please input a inch numbers: "))
# length = (feet * 12 + inch) * 2.54
# print ("the length of two points im kilometer is: %.2f" % length)

#练习15 距离单位
# _feet = float(input("please input a feet numbers: "))
# _inch = 12 * _feet
# _mile = _feet / 5280
# _yard = _feet / 3
# print ("the length in inch is: %.2f" % _inch)
# print ("the length in mile is: %.2f" % _mile)
# print ("the length in yard is: %.2f" % _yard)

#练习16 面积和体积
# r = float(input("please input a radius numbers: "))
# A = math.pi * r ** 2
# V = (4/3) * math.pi * r **3
# print ("the area  is: %.2f" % A, "     ","the volume is: %.2f" % V)

#练习17 比热容
# m = float(input("please input a quality numbers: "))
# delta_T = float(input("please input a delta temperature numbers: "))
# C = 4.186
# Q = C * m * delta_T
# print ("the heat is: %.2f" % Q)

#练习18 圆柱体的体积
# r = float(input("please input a radius numbers: "))
# h = float(input("please input a height numbers: "))
# V = math.pi * (r ** 2) * h
# print ("the volume is: %.2f" % V)

#练习19 自由落体
# _v = float(input("please input a speed numbers: "))
# _a = float(input("please input a acceleration numbers: "))
# _d = float(input("please input a length numbers: "))
# v_f = (_v ** 2 + 2 * _a * _d ) ** 0.5
# print ("the final speed is: %.2f" % v_f)

#练习20 理想气体定律
# _p = float(input("please input a pressure numbers: "))
# _v = float(input("please input a volume numbers: "))
# _T = float(input("please input a temperature numbers: "))
# _p1 = _p * 10000
# _v1 = _v * 0.001
# _T1 = (_T-32) * (9 / 5) + 273.15
# R = 8.314
# n = (_p1 * _v1) / (R * _T1)
# print ("the number is: %.2f" % n)

#练习21 三角形的面积
# b = float(input("please input a numbers: "))
# h = float(input("please input a numbers: "))
# area = 0.5 * b * h
# print ("the number is: %.2f" % area)

#练习22 三角形的面积
# s_1 = float(input("please input a numbers: "))
# s_2 = float(input("please input a numbers: "))
# s_3 = float(input("please input a numbers: "))
# _s = (s_1 + s_2 + s_3) / 2
# area = (_s * (_s - s_1) * (_s- s_2) * (_s - s_3)) ** 0.5
# print ("the number is: %.2f" % area)

#练习23 正多边形的面积
# _s = float(input("please input a numbers: "))
# _n = float(input("please input a numbers: "))
# area = (_n * _s ** 2) / (4 * (math.pi / _n))
# print ("the number is: %.2f" % area)

#练习24 计算持续的时间
# _day = float(input("please input a numbers: "))
# _hour = float(input("please input a numbers: "))
# _minute= float(input("please input a numbers: "))
# _second = float(input("please input a numbers: "))
# all_second = (((_day * 24) + _hour) * 60 + _minute) * 60 + _second
#print ("the number is: %.2f" % all_second)
# print ("the number is: ",
#        "%d : %02d : %02d : %02d." % (_day,_hour,_minute,_second))

#练习25 时间单位
# second = int(input("please input a time number in second: "))
# _second = second % 60
# a = second / 60
# _minute = a % 60
# b = a / 60
# _hour = b % 60
# _day = b / 60
# print("the time is:","%.d:%.02d:%.02d:%.02d" % (_day,_hour,_minute,_second))

#练习26 当前时间
# _time_now = time.asctime()
# print(_time_now)

#练习27 复活节在什么时候
# _year = int(input("please input this year: "))
# a = _year % 19
# b = int(_year / 100)
# c = _year % 100
# d = int(b / 4)
# e = b % 4
# f = int((b + 8) / 25)
# g = int((b - f + 1) / 3)
# h = (19 * a + b - d - g + 15) % 30
# i = int(c / 4)
# k = c % 4
# l = (32 + 2 * e + 2 * i - h - k) % 7
# m = int((a + 11 * h + 22 * l) / 451)
# month = int((h + l - 7 * m + 114) / 31)
# day = (h + l - 7 * m + 114) % 31
# print("the Easter festival is: %.02d month   %.02d day" % (month,day))

#练习28 身体质量指数
# height = float(input("please input the height in meter: "))
# weight = float(input("please input the weight in kg: "))
# BMI = weight / (height * weight)
# print("the BMI is： %.2f" % BMI)

#练习29 风寒
# _T = float(input("please input the temperature: "))
# _v = float(input("please input the speed: "))
# WCI = 13.12 + 0.6215 * _T - 11.37 * _v ** 0.16 + 0.3965 * _T * _v ** 0.16
# print("the WCI is： %.2f" % WCI)

#练习30 摄氏温度转换成华氏温度和开尔文温度

#练习31 压力的单位

#练习32 整数中各个数字的和
# number = int(input("请输入一个四位整数： "))
# a = int(number / 1000)
# b = int((number - a * 1000) / 100)
# c = int((number - a * 1000 - b * 100) / 10)
# d = int(number - a * 1000 - b * 100 - c *10)
# _sum = a + b + c + d
# print("the sum is: %.d" % _sum)

#练习33 对3个整数排序
# a = int(input("please input a int number: "))
# b = int(input("please input a int number: "))
# c = int(input("please input a int number: "))
# _sum = (a,b,c)
# _max = max(_sum)
# _min = min(_sum)
# _center = (a +b + c) - _max - _min
# print("三个数的大小次序（从大到小）：%.d > %.d > %.d " % (_max,_center,_min))

#练习34 旧面包
_number = int(input("please input the number of buying bread； "))
_price = _number * 3.49
_discount_price = _price * 0.6
print("the price of bread is: %.2f" % _price)
print("the discount price of bread is: %.2f" % _discount_price)







