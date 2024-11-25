# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mergeList.py
# Time       ：2024/11/24 20:33
# Author     ：author name
# version    ：python 3.6
# Description：
"""
class Node(object):

    def __init__(self, item=None, next_=None):

        self.item = item
        self.next = next_

def merge_sin_link_list(l1, l2):

    if not l1:
        return l2
    if not l2:
        return l1

    cur = None

    if l1.item < l2.item:
        cur = l1
        cur.next = merge_sin_link_list(l1.next, l2)
    else:
        cur = l2
        cur.next = merge_sin_link_list(l1, l2.next)

    return cur


if __name__ == "__main__":

    l1 = Node(1)
    l2 = Node(2)
    l3 = Node(3)
    l4 = Node(4)
    l5 = Node(5)
    l6 = Node(6)

    l1.next = l3
    l3.next = l5

    l2.next = l4
    l4.next = l6

    print(l1.item, l1.next.item)

    l = merge_sin_link_list(l1, l2)

    print(l.item, l.next.item)