# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : rotateBox.py
# Time       ：2024/11/23 13:26
# Author     ：author name
# version    ：python 3.6
# Description：
"""


class Solution(object):

    def rotateBox(self, box: list[list[str]]) -> list[list[str]]:
        print(box)

        m, n = len(box), len(box[0])

        rotated_box = [['.' for _ in range(m)] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        # print(rotated_box)

        for row in rotated_box:
            empty_space = 0
            for i, cell in enumerate(row):
                if cell == ".":
                    empty_space += 1
                elif cell == "#":
                    if empty_space > 0:
                        row[i] = "."
                        row[i - empty_space] = "#"
                        empty_space -= 1

        # [['#', '.', '#']]
        # [['#'], ['.'], ['#']]

        # for row in rotated_box:
        #     for i, cell in enumerate(row):

        print(rotated_box)
        return rotated_box


# box = [['#', '.', '*']]
box = [['#', '.', '#']]

test1 = Solution()
test1.rotateBox(box)
