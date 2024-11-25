#
# class CuteCat:
#
#     def __init__(self):
#         self.name = "Lambart"
#
# cat1 = CuteCat()
# print(cat1.name)

class CuteCat:

    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print(f"{self.name} said: I am {self.age} years old")


cat2 = CuteCat("Roal", 5, "RED")
# print(cat2.age)
cat2.speak()
