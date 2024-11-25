# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Practise001.py
# Time       ：2024/11/23 19:25
# Author     ：author name
# version    ：python 3.6
# Description：字符串验证重复
"""


class Solution(object):

    def isUnique1(self, s1: str) -> bool:
        diff = True
        slist = list(s1)

        for i in range(len(slist)):
            for j in range(i + 1, len(slist)):
                if slist[i] == slist[j]:
                    diff = False
        return diff

    def isUnique2(self, s1):

        li = []
        for s in s1:
            if s not in li:
                li.append(s)
            else:
                return False
        return True

        # if len(li) == len(s1):
        #     return True
        # else:
        #     return False

    def isUnique3(self, str):
        se = set(str)  # set类型不允许重复，可以用于去重
        if len(se) != len(str):
            return False
        else:
            return True


s = Solution()
print(s.isUnique1("asds"))
print(s.isUnique2("asd"))
print(s.isUnique3("asd"))
