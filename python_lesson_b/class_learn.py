class A:
    # 类对象, 可以被多个实例共享
    name = "Li Si"

    def __init__(self):
        # 实例对象
        self.name = 'Zhang San'


# a = A()
# print(a.name)

class Date:
    def __init__(self, year, month, day):
        """
        Structure method
        :param year: Year
        :param month: Month
        :param day: Day
        """
        self.year = year
        self.month = month
        self.day = day

    # instance method, all with the parameter "self"
    def __str__(self):
        return f'{self.year}/{self.month}/{self.day}'

    # static method, return current class
    @staticmethod
    def parse_date_string(date_str):
        y, m, d = tuple(date_str.split('-'))
        # 返回类本身, 硬编码，如果类名更改，返回的类名也必须相同
        return Date(int(y), int(m), int(d))

    @classmethod
    def parse_date_str(cls, date_str):
        y, m, d = tuple(date_str.split('-'))
        # cls 参数指向当前类
        return cls(int(y), int(m), int(d))


class User:
    def __init__(self, birthday):
        self.birth = birthday
        self.__birthday = birthday

    def get_age(self):
        return f'Age is: {2024 - self.__birthday.year}'


# 上下文管理器协议
class Sample:
    def __init__(self):
        print("Start con_structure...")

    def __enter__(self):
        # 获取资源
        print("Enter class")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit class")

    def do_something(self):
        print('Doing something')


# 上下文管理器协议
with Sample() as sample:
    sample.do_something()
    pass

# if __name__ == '__main__':

# d1 = Date(2023, 3, 27)
# print(d1)
#
# data_str = '2024-3-27'
# # y, m, d = tuple(data_str.split('-'))  # Split tuple
# # d2 = Date(int(y), int(m), int(d))
# # print(d2)
#
# d3 = Date.parse_date_string(data_str)
# print(f"D3 date is: {d3}")
#
# d4 = Date.parse_date_str(data_str)
# print(f"D4 date is: {d4}")
# print(Date(1985, 4, 1))
# u1 = User(Date(1985, 4, 1))
# # print(u1._User__birthday)
# # print(u1.birth.year)
# # print(u1.get_age())
# print(u1.__dict__)
# print(User.__dict__)
