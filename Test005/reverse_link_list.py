# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : reverse_link_list.py
# Time       ：2024/11/24 20:00
# Author     ：author name
# version    ：python 3.6
# Description：
"""

class Node(object):

    def __init__(self, item=None, next_=None):

        self.item = item
        self.next = next_


def reverseList(head):

    if head == None or head.next == None:
        return head

    pre = None
    next = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


if __name__ == "__main__":

    li = Node(3)
    li.next = Node(4)
    li.next.next = Node(5)
    li.next.next.next = Node(6)

    l = reverseList(li)

    print(l.item, l.next.item, l.next.next.item, l.next.next.next.item)
