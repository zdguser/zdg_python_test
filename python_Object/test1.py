
class Student:    ###Student为类的名称
    native_place = '深圳'   ###直接写在类里面的变量，称为类属性

    def __init__(self,name,age):
        self.name = name    ####self.name 称为实体属性， 进行了一个赋值操作，将局部变量name 赋值给实体属性。
        self.age = age       ###self.name后面.name任取，一般为了统一，与局部变量name统一
        # self.list = list      

    ##实例方法
    def eat(self):
        print('学生在吃饭.....')
        print(self.name + '在吃饭')

    # def sum(self):
    #     alist = self.list
    #     m = len(alist)
    #     s = 0.0
    #     for i in range(m):
    #         s += float(alist[i])
    #     return s
    
    ##静态方法
    @staticmethod
    def method():
        print('我使用了@staticmethod进行修饰,所以我是静态方法,不用self')

    ##类方法
    @classmethod
    def cm(cls):
        print('我是类方法,因为我使用classmethod进行修饰')

stu1 = Student('zhang san',20)
stu2 = Student('Lisi',30)

print(stu1.name)
print(stu1.age)
print(stu1.native_place)

Student.native_place = '北京'
print(stu1.native_place)

###############################
Student.cm()
Student.method()

###################
stu1.eat()

stu1.gender = '女'
print(stu1.gender)