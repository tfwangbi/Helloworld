
# -*- coding:utf-8 -*-

arr = [1, 3, 4, 7, 9, 14, 20, 26, 50, 60, 100, 0]

print("Before:")
for i in range(0, len(arr)-1):
    print(arr[i], end=" ")
print()

number = int(input("Please input a number you want to insert: "))

## Core code

local = 0
for i in range(len(arr)-2, -1, -1):
    if number > arr[i]:
        local = i + 1
        break

for i in range(len(arr)-1, local-1, -1):
    arr[i] = arr[i-1]

arr[local] = number

# print(local)

print("After:")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")
print(arr)