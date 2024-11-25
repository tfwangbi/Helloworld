# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_system.py
# Time       ：2024/11/25 20:21
# Author     ：author name
# version    ：python 3.6
# Description：35 --> 100011
"""

from stack import Stack


def getRemainder(n):
    return n % 2


def traslate10To2(num):

    if num == 0:
        return 0

    nnum = ""
    li = Stack()

    while num >= 1:
        li.push(getRemainder(num))
        num = num // 2


    while not li.is_empty():
        nnum = nnum + str(li.pop())

    return nnum


if __name__ == "__main__":
    print("starts:------------")
    number = 3
    n = traslate10To2(number)
    print(f"Decimal code {number} translate to binary code: {n}")
