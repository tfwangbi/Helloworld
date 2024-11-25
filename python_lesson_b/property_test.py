from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    # 属性装饰器
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

# __getattr__, __getattribute__

    def __getattr__(self, item):
        print("Not found attr")


if __name__ == '__main__':
    user = User("Zhang San", date(year=1985, month=4, day=1))
    # print(user.get_age())

    user.age = 25
    print(user.age)
    print(user._age)
