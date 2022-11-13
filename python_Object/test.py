
class Student:    ###Student为类的名称
    native_place = '深圳'   ###直接写在类里面的变量，称为类属性

    def __init__(self,name,age,list):
        self.name = name    ####self.name 称为实体属性， 进行了一个赋值操作，将局部变量name 赋值给实体属性。
        self.age = age       ###self.name后面.name任取，一般为了统一，与局部变量name统一
        self.list = list      

    ##实例方法
    def eat(self):
        print('学生在吃饭.....')

    def sum(self,list):
        alist = self.list
        m = len(alist)
        s = 0.0
        for i in range(m):
            s += float(alist[i])
        return s
        
    
    
    ##静态方法
    @staticmethod
    def method():
        print('我使用了@staticmethod进行修饰,所以我是静态方法,不用self')

    ##类方法
    @classmethod
    def cm(cls):
        print('我是类方法,因为我使用classmethod进行修饰')

##################################################################################
# stu1 = Student('zhang san',20,list1)
# stu2 = Student('Lisi',30,list1)

# print(stu1.name)
# print(stu1.age)
# print(stu1.native_place)


# stu1.eat()
# A = stu1.eat()
# print(A)
# stu1.method()
# stu1.cm()
####################################################################################
#####调用类里面的方法，方法一
# list1 = [1,2,3,4,5]
# stu3 = Student('zhang',20,list1)
# AA = stu3.sum()
# print('the result is: %d' % AA)

######调用类里面的方法二
# list1 = [1,2,3,4,5,6,7]
# AA = sum(list1)
# print('the result is: %.d' % AA)

################################################################################