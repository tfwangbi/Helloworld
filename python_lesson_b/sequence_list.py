from collections import abc

my_list = []
my_list.append(1)
my_list.append("abd")

my_list.extend((3, 4))
my_list.append((5, 6))
my_list.extend(range(7, 10))

if __name__ == '__main__':
    print(my_list)
    print(my_list[::-1])
    print(my_list[::2])
    print(my_list[1::2])
    print(my_list[::3])
    print(my_list[2:4])
    my_list[len(my_list):] = [10]
    print(my_list)
