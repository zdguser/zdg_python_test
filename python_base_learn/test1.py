def square(_a,_b,_c):
    _list = []
    _list.append(_a)
    _list.append(_b)
    _list.append(_c)
    _list.sort()
    _cost = float(_list[1])
    return _cost
if __name__ == "__main__":
  _a = float(input("please input the number: "))
  _b = float(input("please input the number: "))
  _c = float(input("please input the number: "))

  _d = square(_a,_b,_c) + 1.00
  print("中间数为：%.2f " % _d)