# class Human:
#     def __init__(self, person):
#         self.name = person["name"]
#         self.age = person["age"]
#         self.sex = person["sex"]
#
#     def speak(self):
#         pass
#
#     def read(self):
#         pass
#
#     def breathe(self):
#         print(f"{self.name} is breathing.")
#
#
# zhsinfo = {
#     'name': 'ZhangSan',
#     'age': 30,
#     'sex': 'male'
# }
# zhangsan = Human(zhsinfo)
# zhangsan.breathe()


# Inherit structure
class Mammal:   ## parent class
    def __init__(self, mammal_info):
        self.name = mammal_info['name']
        self.age = mammal_info['age']
        self.sex = mammal_info['sex']
        self.num_eyes = 2

    def breathe(self):
        print(f'{self.name} is breathing.')

    def poop(self):
        print(self.name + ' is pooping.')


class Human(Mammal):

    def __init__(self, mammal_info):
        super().__init__(mammal_info)
        self.has_tail = False
    def read(self):
        print(self.name + ' is reading a book.')


class Cat(Mammal):

    # Child class
    def __init__(self, mammal_info):
        super().__init__(mammal_info)
        self.tail = True

    def scratch_soft(self):
        print(self.name + ' is scratching soft.')

    def poop(self):

        print(f'{self.name} is so trouble, he is pooping on the soft')

zhsinfo = {
    'name': 'ZhangSan',
    'age': 30,
    'sex': 'male'
}

zs = Human(zhsinfo)
zs.read()
zs.poop()

catinfo = {
    'name': 'Pretty',
    'age': 3,
    'sex': 'male'
}
cat_pretty = Cat(catinfo)

cat_pretty.scratch_soft()
cat_pretty.breathe()
cat_pretty.poop()