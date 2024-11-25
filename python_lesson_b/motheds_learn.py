class Student:
    def __init__(self, student_list):
        self.student = student_list

    def __getitem__(self, item):
        return self.student[item]

    def __str__(self):
        return '...'.join(self.student)

class Nums:
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


if __name__ == '__main__':
    student = Student(['Zhang San', 'Li Si', 'Wang Wu'])

    # for item in student.student:
    #     print(item)

    for i in student:
        print(i)

    print(student)
    print("Case 2------------------")

    num1 = Nums(-5)
    print(abs(num1))
