from test import Student

def main():
    alist = [1,2,3,4,5,6,7,8,9,10]
    stu1 = Student('zhang',20,alist)
    res1 = stu1.sum(alist)
    print('the new result is: %.d',res1)

if __name__ == '__init__':
    main()