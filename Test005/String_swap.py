# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : String_swap.py
# Time       ：2024/11/22 16:32
# Author     ：author name
# version    ：python 3.6
# Description：
"""


class Solution(object):

    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        dif1 = []
        dif2 = []

        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                dif1.append(s1[i])
                dif2.append(s2[i])

                if len(dif1) > 2:
                    return False

        if len(dif1) == 0 and len(dif2) == 0:
            return True
        elif len(dif1) == 1 and len(dif2) == 1:
            return False
        return dif1[0] == dif2[1] and dif2[0] == dif1[1]

    def areAlmostEqual2(self, str1: str, str2: str) -> bool:

        # pass
        s1 = list(str1)
        s2 = list(str2)

        s1.sort()
        s2.sort()

        pos = 0
        res = True
        while pos < len(s1) and res:
            if s1[pos] == s2[pos]:
                pos = pos + 1
            else:
                res = False

        print(res)

        return res


test1 = Solution()
test1.areAlmostEqual("bank", "knab")
test1.areAlmostEqual2("bank", "knas")
