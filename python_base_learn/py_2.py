#import math

#练习35 偶数还是奇数
# number = int(input("please input a int number: "))
# if (number % 2) == 0:
#    result = "the number is even number!"
# else:
#    result = "the number is odd number!"
# print(result)

#练习36 狗年
# _man_year = float(input("please input  the man year: "))
# if _man_year < 0:
#     result = "wrong message!"
# elif _man_year >= 0 and _man_year <= 2:
#     result = _man_year * 10.5
# else:
#     result = (_man_year - 2) * 4 + 10.5 * 2
#
# print(result)

#练习37 元音或辅音
# _num = input("please input a letter: ")
# if _num == 'a' or _num == 'e' or _num == 'i' or _num == 'o' or _num == 'u':
#     result = "that is a vowel letter!"
# elif _num == "y":
#     result = "that maybe a vowel letter or a consonants letter!"
# else:
#     result = "that is a consonants letter!"
# print(result)

#练习38 形状的命名
# _num = int(input("please input a int number: "))
# if _num <= 10 and _num >= 3:
#     print("这是一个 %.d 边形 !" % _num)
# else:
#     result = "wrong message!"
#     print(result)

#练习39 月名到天数
# _num = int(input("please input a month number: "))
# _num = input("please input a month: ")
# if _num == 'jan':
#     print("this month have 31 days")
# elif _num == 'feb':
#     print("this month have 28 days")
# elif _num == 'mar':
#     print("this month have 31 days")
# elif _num == 'apr':
#     print("this month have 30 days")
# elif _num == 'may':
#     print("this month have 31 days")
# elif _num == 'jun':
#     print("this month have 30 days")
# elif _num == 'jul':
#     print("this month have 31 days")
# elif _num == 'aug':
#     print("this month have 31 days")
# elif _num == 'sep':
#     print("this month have 30 days")
# elif _num == 'oct':
#     print("this month have 31 days")
# elif _num == 'nov':
#     print("this month have 30 days")
# elif _num == 'dec':
#     print("this month have 31 days")
# else:
#     print("wrong message!")

#练习40 音量
# _num = int(input("please pnput a number: "))
# if _num == 130:
#     print("这个声音分贝等于手提钻! ")
# elif _num == 106:
#     print("这个声音分贝等于割草机! ")
# elif _num == 70:
#     print("这个声音分贝等于闹钟! ")
# elif _num == 40:
#     print("这个声音分贝等于安静房间! ")
# elif _num > 40 and _num < 70:
#     print("这个声音分贝大于安静房间，小于闹钟! ")
# elif _num > 70 and _num < 106:
#     print("这个声音分贝大于闹钟，小于割草机! ")
# elif _num > 106 and _num < 130:
#     print("这个声音分贝大于割草机，小于手提钻! ")
# else:
#     print("这个声音分贝无法比较! ")

#练习41 三角形的分类
# a = input("please input a number: ")
# b = input("please input a number: ")
# c = input("please input a number: ")
# if a == b and b == c and a == c:
#     print("这是一个等边三角形.")
# elif (a == b) or (b == c) or (a == c):
#     print("这是一个等腰三角形.")
# elif ((a + b)<=c) or ((c + b)<=a) or ((a + c)<=b):
#     print("这是一个错误输入.")
# else:
#     print("这是一个不等边三角形.")

#练习42 音符的频率
# _num = input("请输入一个音符: ")
# if _num[0] == 'C':
#    if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#        result = 261.63 / 2 **(4 -int(_num[1]))
#        print("音符的频率为： %.2f  Hz" % result)
#    else:
#        print("wrong message.")
# elif _num[0] == 'D':
#     if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#         result = 293.66 / 2 ** (4 - int(_num[1]))
#         print("音符的频率为： %.2f  Hz" % result)
#     else:
#         print("wrong message.")
# elif _num[0] == 'E':
#     if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#         result = 329.63 / 2 ** (4 - int(_num[1]))
#         print("音符的频率为： %.2f  Hz" % result)
#     else:
#         print("wrong message.")
# elif _num[0] == 'F':
#     if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#         result = 349.23 / 2 ** (4 - int(_num[1]))
#         print("音符的频率为： %.2f  Hz" % result)
#     else:
#         print("wrong message.")
# elif _num[0] == 'G':
#     if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#         result = 392.00 / 2 ** (4 - int(_num[1]))
#         print("音符的频率为： %.2f  Hz" % result)
#     else:
#         print("wrong message.")
# elif _num[0] == 'A':
#     if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#         result = 440.00 / 2 ** (4 - int(_num[1]))
#         print("音符的频率为： %.2f  Hz" % result)
#     else:
#         print("wrong message.")
# elif _num[0] == 'B':
#     if (int(_num[1]) >= 0) and (int(_num[1]) <= 8):
#         result = 493.88 / 2 ** (4 - int(_num[1]))
#         print("音符的频率为： %.2f  Hz" % result)
#     else:
#         print("wrong message.")
# else:
#     print("wrong message.")

#练习43 音符频率的逆转换
# _f = float(input("please input a number: "))
# if (_f >= 260.63) and (_f <= 263.63):
#     print("that is C4")
# elif (_f >= 292.66) and (_f <= 294.66):
#     print("that is D4")
# elif (_f >= 328.63) and (_f <= 330.63):
#     print("that is E4")
# elif (_f >= 348.23) and (_f <= 350.23):
#     print("that is F4")
# elif (_f >= 391.00) and (_f <= 393.00):
#     print("that is G4")
# elif (_f >= 439.00) and (_f <= 441.00):
#     print("that is A4")
# elif (_f >= 492.88) and (_f <= 494.88):
#     print("that is B4")
# else:
#     print("wrong message")

#练习44 钞票上的脸
# _num = int(input("please input a number: "))
# if _num == 1:
#     print("1美元的是乔治 华盛顿")
# elif _num == 2:
#     print("2美元的是托马斯 杰斐逊")
# elif _num == 5:
#     print("5美元的是林肯")
# elif _num == 10:
#     print("10美元的是汉密尔顿")
# elif _num == 20:
#     print("20美元的是杰克逊")
# elif _num == 50:
#     print("50美元的是格兰特")
# elif _num == 100:
#     print("100美元的是富兰克林")
# else:
#     print("wrong message")

#练习45 假日的日期
# _num = input("please input a date,like 0504: ")
# if int(_num[1]) == 1:
#     if int(_num[3]) == 1:
#        print("the date is 元旦")
#     else:
#        print("the date is not festival")
# elif int(_num[1]) == 7:
#     if int(_num[3]) == 1:
#        print("the date is 国庆日")
#     else:
#        print("the date is not festival")
# elif (int(_num[0]) == 1) and (int(_num[1]) == 2):
#     if (int(_num[2]) == 2) and (int(_num[3]) == 5):
#        print("the date is 圣诞节")
#     else:
#        print("the date is not festival")
# else:
#     print("the date is not festival")

#练习46 哪个正方形是什么颜色？
# _num = input("please input a location, like a1: ")
# if _num[0] == 'a' or _num[0] == 'c' or _num[0] == 'e' or _num[0] == 'g':
#     if int(_num[1]) == 1 or int(_num[1]) == 3 or int(_num[1]) == 5 or int(_num[1]) == 7:
#         print("the location is black.")
#     elif int(_num[1]) == 2 or int(_num[1]) == 4 or int(_num[1]) == 6 or int(_num[1]) == 8:
#         print("the location is white.")
#     else:
#         print("wrong message.")
# elif _num[0] == 'b' or _num[0] == 'd' or _num[0] == 'f' or _num[0] == 'h':
#     if int(_num[1]) == 1 or int(_num[1]) == 3 or int(_num[1]) == 5 or int(_num[1]) == 7:
#         print("the location is white.")
#     elif int(_num[1]) == 2 or int(_num[1]) == 4 or int(_num[1]) == 6 or int(_num[1]) == 8:
#         print("the location is black.")
#     else:
#         print("wrong message.")
# else:
#     print("wrong message.")

#练习47 季节的确定
# _date = input("please input a date, like 0101: ")
# _month = int(_date[0]) * 10 + int(_date[1])
# _day = int(_date[2]) * 10 + int(_date[3])
# if _month == 1:
#     print(" that is winter.")
# elif _month == 2:
#     print(" that is winter.")
# elif _month == 3:
#     if (_day < 20) and (_day >= 1):
#        print(" that is winter.")
#     elif (_day >= 20) and (_day <= 31):
#        print(" that is spring.")
#     else:
#        print("wrong message")
# elif _month == 4:
#     print(" that is spring.")
# elif _month == 5:
#     print(" that is spring.")
# elif _month == 6:
#     if (_day < 21) and (_day >= 1):
#         print(" that is spring.")
#     elif (_day >= 21) and (_day <= 30):
#         print(" that is summer.")
#     else:
#         print("wrong message")
# elif _month == 7:
#     print(" that is summer.")
# elif _month == 8:
#     print(" that is summer.")
# elif _month == 9:
#     if (_day < 22) and (_day >= 1):
#         print(" that is summer.")
#     elif (_day >= 22) and (_day <= 30):
#         print(" that is autumn.")
#     else:
#         print("wrong message")
# elif _month == 10:
#     print(" that is autumn.")
# elif _month == 11:
#     print(" that is autumn.")
# elif _month == 12:
#     print(" that is winter.")
# else:
#     print("wrong message")

#练习48 出生日期到星座的对应
# _num = input("please input the date, like 0502: ")
# _month = int(_num[0]) * 10 + int(_num[1])
# _day = int(_num[2]) * 10 + int(_num[3])
# if _month == 1:
#    if (_day >=1) and  (_day <= 19):
#        print("你是摩羯座")
#    elif (_day >=20) and  (_day <= 31):
#        print("你是水瓶座")
#    else:
#        print("输入错误")
# elif _month == 2:
#    if (_day >=1) and  (_day <= 18):
#        print("你是水瓶座")
#    elif (_day >=19) and  (_day <= 29):
#        print("你是双鱼座")
#    else:
#        print("输入错误")
# elif _month == 3:
#    if (_day >=1) and  (_day <= 20):
#        print("你是双鱼座")
#    elif (_day >=21) and  (_day <= 31):
#        print("你是白羊座")
#    else:
#        print("输入错误")
# elif _month == 4:
#    if (_day >=1) and  (_day <= 19):
#        print("你是白羊座")
#    elif (_day >=20) and  (_day <= 30):
#        print("你是金牛座")
#    else:
#        print("输入错误")
# elif _month == 5:
#    if (_day >=1) and  (_day <= 20):
#        print("你是金牛座")
#    elif (_day >=21) and  (_day <= 31):
#        print("你是双子座")
#    else:
#        print("输入错误")
# elif _month == 6:
#    if (_day >=1) and  (_day <= 20):
#        print("你是双子座")
#    elif (_day >=21) and  (_day <= 30):
#        print("你是巨蟹座")
#    else:
#        print("输入错误")
# elif _month == 7:
#    if (_day >=1) and  (_day <= 22):
#        print("你是巨蟹座")
#    elif (_day >=23) and  (_day <= 31):
#        print("你是狮子座")
#    else:
#        print("输入错误")
# elif _month == 8:
#    if (_day >=1) and  (_day <= 22):
#        print("你是狮子座")
#    elif (_day >=23) and  (_day <= 31):
#        print("你是处女座")
#    else:
#        print("输入错误")
# elif _month == 9:
#    if (_day >=1) and  (_day <= 22):
#        print("你是处女座")
#    elif (_day >=23) and  (_day <= 30):
#        print("你是天秤座")
#    else:
#        print("输入错误")
# elif _month == 10:
#    if (_day >=1) and  (_day <= 22):
#        print("你是天秤座")
#    elif (_day >=23) and  (_day <= 31):
#        print("你是天蝎座")
#    else:
#        print("输入错误")
# elif _month == 11:
#    if (_day >=1) and  (_day <= 21):
#        print("你是天蝎座")
#    elif (_day >=22) and  (_day <= 30):
#        print("你是射手座")
#    else:
#        print("输入错误")
# elif _month == 12:
#    if (_day >=1) and  (_day <= 22):
#        print("你是射手座")
#    elif (_day >=23) and  (_day <= 31):
#        print("你是天蝎座")
#    else:
#        print("输入错误")
# else:
#     print("输入错误")

#练习49 十二生肖
# _num = input("please input a year, like 2012: ")
# a = int(_num[0])
# b = int(_num[1])
# c = int(_num[2])
# d = int(_num[3])
# _year = a * 1000 + b * 100 + c * 10 + d
# _delta = abs(_year - 0)
# _n = _delta % 12
# if _n == 0:
#     print("今年是猴年！")
# elif _n == 1:
#     print("今年是鸡年！")
# elif _n == 2:
#     print("今年是狗年！")
# elif _n == 3:
#     print("今年是猪年！")
# elif _n == 4:
#     print("今年是鼠年！")
# elif _n == 5:
#     print("今年是牛年！")
# elif _n == 6:
#     print("今年是虎年！")
# elif _n == 7:
#     print("今年是兔年！")
# elif _n == 8:
#     print("今年是龙年！")
# elif _n == 9:
#     print("今年是蛇年！")
# elif _n == 10:
#     print("今年是马年！")
# elif _n == 11:
#     print("今年是羊年！")

#练习50 里氏地震

#练习51 二次函数的根
# a,b,c = input("please input three numbers, like 10 11 12: ").split()
# _a = int(a[0])
# a = float(input("please input a number: "))
# b = float(input("please input a number: "))
# c = float(input("please input a number: "))
# _delta = b ** 2 - 4 * a * c
# if _delta < 0:
#     print("没有实数根")
# elif int(_delta) == 0:
#     _root = (-b) / (2 * a)
#     print("有1个实数根"," ", "实数根的值为： %.2f " % _root)
# elif _delta > 0:
#     _root_1 = ((-b) + (_delta) ** 0.5) / (2 * a)
#     _root_2 = ((-b) - (_delta) ** 0.5) / (2 * a)
#     print("有2个实数根"," ", "实数根的值分别为： %.2f， %.2f " % (_root_1,_root_2))

#练习52 字母等级到绩点
# _num = input("请输入成绩等级： ")
#
# if _num == 'A+':
#    print("成绩是4.0")
# elif _num == 'A-':
#    print("成绩是3.7")
# elif _num == 'A':
#    print("成绩是3.9")

#练习53 绩点到到字母等级


#练习54 评估员工业绩

#练习55 可见光的波长

#练习56 按频率来命名


#手机账单
# _time = int(input("请输入手机通话时长（分钟）: "))
# _message = int(input("请输入手机文本消息（条）: "))
# if(_time <= 50) and (_message <= 50 ):
#   _cost = (15 + 0.44) * (1 + 0.05)
#   _tax =  (15 + 0.44) * 0.05
#   print("手机账单总花费为： %.2f 美元" % _cost)
#   print("手机账单基本花费为：15 美元")
#   print("手机账单额外时长费用为：0 美元" )
#   print("手机账单额外短信费用为：0 美元")
#   print("手机账单的税务费用为：%.2f 美元" % _tax)
# elif (_time <= 50) and (_message > 50 ):
#     _cost = (15 + 0.44 + (_message - 50) * 0.15) * (1 + 0.05)
#     _tax = (15 + 0.44 + (_message - 50) * 0.15) * 0.05
#     _cost_message = (_message - 50) * 0.15
#     print("手机账单总花费为： %.2f 美元" % _cost)
#     print("手机账单基本花费为：15 美元")
#     print("手机账单额外时长费用为：0 美元")
#     print("手机账单额外短信费用为：%.2f 美元" % _cost_message)
#     print("手机账单的税务费用为：%.2f 美元" % _tax)
# elif (_time > 50) and (_message <= 50 ):
#     _cost = (15 + 0.44 + (_time - 50) * 0.25) * (1 + 0.05)
#     _tax = (15 + 0.44 + (_time - 50) * 0.25) * 0.05
#     _cost_time = (_time - 50) * 0.25
#     print("手机账单总花费为： %.2f 美元" % _cost)
#     print("手机账单基本花费为：15 美元")
#     print("手机账单额外时长费用为：%.2f 美元" % _cost_time)
#     print("手机账单额外短信费用为：0 美元")
#     print("手机账单的税务费用为：%.2f 美元" % _tax)
# elif (_time > 50) and (_message > 50 ):
#     _cost = (15 + 0.44 + (_time - 50) * 0.25 + (_message - 50) * 0.15) * (1 + 0.05)
#     _tax = (15 + 0.44 + (_time - 50) * 0.25 + (_message - 50) * 0.15) * 0.05
#     _cost_time = (_time - 50) * 0.25
#     _cost_message = (_message - 50) * 0.15
#     print("手机账单总花费为： %.2f 美元" % _cost)
#     print("手机账单基本花费为：15 美元")
#     print("手机账单额外时长费用为：%.2f 美元" % _cost_time)
#     print("手机账单额外短信费用为：%.2f 美元" % _cost_message)
#     print("手机账单的税务费用为：%.2f 美元" % _tax)

#练习58 这是闰年吗？

#练习59 第二天
# year = input("please input the year like 2012: ")
# month = input("please input the month like 05: ")
# day = input("please input the day like 06: ")
#
# _year = 1000 * int(year[0]) + 100 * int(year[1]) + 10 * int(year[2]) + int(year[3])
# _month = 10 * int(month[0]) + int(month[1])
# _day = 10 * int(day[0]) + int(day[1])
#
# if (_month == 12) and (_day == 31):
#     _year = _year + 1
#     print("%d " % _year,"年" ,"1月  1日")
# elif (_day == 31) and (_month == 1 or _month == 3 or _month == 5 or _month == 7 or _month == 8 or _month == 10):
#     _month = _month + 1
#     print("%d " % _year,"年","%d " % _month, "月" ," 1日")
# elif (_day == 30) and (_month == 4 or _month == 6 or _month == 9 or _month== 11):
#     _month = _month + 1
#     print("%d " % _year,"年","%d " % _month, "月" ," 1日")
# elif (_day == 28) and (_month == 2):
#     _month = _month + 1
#     print("%d " % _year,"年","%d " % _month, "月" ," 1日")
# else:
#     _day = _day + 1
#     print("%d " % _year, "年", "%d " % _month, "月",  "%d " % _day, "日")

#练习60 1月1日是星期几

#练习61 车牌有效吗
# _num = input("please input your car number: ")
# _n = len(_num)
# if _n == 6:
#    if (_num[0].isdigit() == 1) and  (_num[1].isdigit() == 1) and (_num[2].isdigit() == 1) \
#    and (_num[3].isalpha() == 1) and (_num[4].isalpha() == 1) and (_num[5].isalpha() == 1):
#        print("old car number.")
#    else:
#        print("wrong message.")
# elif _n == 7:
#     if (_num[0].isdigit() == 1) and (_num[1].isdigit() == 1) and (_num[2].isdigit() == 1) \
#             and (_num[3].isalpha() == 1) and (_num[4].isalpha() == 1) and (_num[5].isalpha() == 1) and (_num[6].isalpha() == 1):
#         print("old car number.")
#     else:
#         print("wrong message.")
# else:
#     print("wrong message")




#练习62 轮盘赌
# _num = input("please input a number: ")
# if (_num == '0') and (_num == '00'):
#     print("nothing")
# elif (_num == '1') or (_num == '3') or (_num == '5')\
# or (_num == '7') or (_num == '9') or (_num == '12')\
# or (_num == '14') or (_num == '16') or (_num == '18') \
# or (_num == '19') or (_num == '21') or (_num == '23') \
# or (_num == '25') or (_num == '27') or (_num == '32') \
# or (_num == '34') or (_num == '36'):
#     print("pay ",_num)
#     print("pay ","red")
#     _num1 = int(_num,10)
#     if _num1 % 2 == 0:
#         print("pay ","even")
#     elif _num1 % 2 == 1:
#         print("pay ", "odd")
#     if _num1 >= 19:
#         print("pay ","19 to 36")
#     elif _num1 <= 18:
#         print("pay ","1 to 18")
#
# elif (_num == '1') or (_num == '3') or (_num == '5')\
# or (_num == '7') or (_num == '9') or (_num == '12')\
# or (_num == '14') or (_num == '16') or (_num == '18') \
# or (_num == '19') or (_num == '21') or (_num == '23') \
# or (_num == '25') or (_num == '27') or (_num == '32') \
# or (_num == '34') or (_num == '36'):
#     print("pay ", _num)
#     print("pay ", "black")
#     _num1 = int(_num, 10)
#     if _num1 % 2 == 0:
#         print("pay ", "even")
#     elif _num1 % 2 == 1:
#         print("pay ", "odd")
#     if _num1 >= 19:
#         print("pay ", "19 to 36")
#     elif _num1 <= 18:
#         print("pay ", "1 to 18")