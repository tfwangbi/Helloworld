# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : strCompress.py
# Time       ：2024/11/23 20:50
# Author     ：author name
# version    ：python 3.6
# Description：
"""


class Solution(object):

    def compress(self, strs):
        li = []
        count = 1
        strs += " "
        for i in range(len(strs) - 1):

            if strs[i] == strs[i + 1]:
                count += 1
            else:
                li.append([strs[i], count])
                count = 1
        # print(li)

        newstr = ''

        for j in li:
            # print(j[1])
            newstr += j[0] + str(j[1])
        # print(newstr)

        if len(newstr) >= len(strs):
            return strs
        else:
            return newstr


s = Solution()
print(s.compress("ssssdasdasdsaaaaaaaaaaaaaaaaads"))
