# -*- coding: utf-8 -*-
# () 相当于执行语句, 实例化语句

def print_name(name = 'Jason'):
    print(name)

class Person:
    def __init__(self):
        print('Test this class')

# f1 = print_name
# f1('Lili')
#
# my_class1 = Person  #set Class to a parameter
# my_class1()  # () is execution

obj_list = []
obj_list.append(print_name)
obj_list.append(Person)
# obj_list[0]()
# for fun in obj_list:
#     fun()

# 装饰器
def decorator_func():
    print("function starts...")
    return print_name
my_func_return = decorator_func()
my_func_return("This is a decorator")

#------------------------------------------------------

a = 1
b = "abc"
class Student:
    pass
stu = Student()

print(type(a))
print(type(b))
print(type(stu))
print(type(Student))
print(str.__bases__)
print(int.__bases__)
# print(Student.__bases__)
print(f'Student bases from {Student.__bases__}')
print(f'Object bases from {object.__bases__}')  #object不继承自任何类，object是由type创建的，type又继承自object,两者是互补关系
print(type(object))
print(f'type bases from {type.__bases__}')  #type 本身也是object
print(type(type))  #type自身创建了自身（type）
