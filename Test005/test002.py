# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test002.py
# Time       ：2024/11/24 15:05
# Author     ：author name
# version    ：python 3.6
# Description：
"""


class StringSwap(object):

    def __init__(self, s: str, pos: int):
        self.str = s
        self.pos = pos
        self.strSwap()

    def strSwap(self):

        if self.pos <= 0:
            print(self.str)
            return self.str
        else:
            s1 = self.str[:self.pos]
            s2 = self.str[self.pos:]

            print(s2 + s1)
            return s2 + s1

        # for i in range(0, len(nl)):
        #     if i < self.pos:
        #         letter = nl[i]
        #         nl.remove(letter)
        #         nl.append(letter)


str1 = StringSwap("abcdefgh", 10)
