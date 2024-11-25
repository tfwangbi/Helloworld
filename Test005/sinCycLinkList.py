# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : sinCycLinkList.py
# Time       ：2024/11/24 18:35
# Author     ：author name
# version    ：python 3.6
# Description：
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        # next note
        self.next = None


class SinCycLinkList(object):

    def __init__(self, node=None):
        # 头部域 空链表 = None
        self.__head = None

        if node:
            node.next = node
            self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):

        if self.is_empty():
            return 0
        else:
            cur = self.__head
            count = 1

            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):

        if self.is_empty():
            return

        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item)

    def add(self, item):
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            node.next = self.__head
            cur.next = node
            self.__head = node

    def append(self, item):

        if self.is_empty():
            self.add(item)
        else:
            node = Node(item)
            cur = self.__head

            if cur.next == self.__head:
                node.next = cur
                cur.next = node
                return
            else:
                while cur.next != self.__head:
                    cur = cur.next

                node.next = cur.next
                cur.next = node

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)

            pre = self.__head
            count = 0
            while count < pos - 1:
                pre = pre.next
                count += 1

            node.next = pre.next
            pre.next = node

    def delete(self, item):

        text = "No Value"
        cur = self.__head
        pre = None
        if self.is_empty():
            return text

        if cur.item == item:
            if cur.next != self.__head:
                while cur.next != self.__head:
                    cur = cur.next
                cur.next = self.__head.next
                self.__head = self.__head.next
                text = "Delete success. [0]"
            else:
                self.__head = None
                text = "Delete success. [1]"
        else:
            while cur.next != self.__head:
                if cur.item == item:
                    pre.next = cur.next
                    text = "Delete success. [2]"
                    return text
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = self.__head
                text = "Delete success. [3]"

        return text


if __name__ == "__main__":
    node1 = None

    sl = SinCycLinkList(node1)

    sl.add(20)
    sl.add(30)
    sl.add(6000)
    sl.append(200)
    sl.append(300)
    sl.insert(3, 333)
    sl.insert(1, 222)
    sl.insert(100, 777)
    # sl.insert(0, 444)
    print(sl.delete(777))
    sl.travel()

    print(f'Length of the Link List: {sl.length()}')
