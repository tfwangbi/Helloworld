# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : doubleLinkList.py
# Time       ：2024/11/24 13:32
# Author     ：author name
# version    ：python 3.6
# Description：
"""

from SingleNote import SingleLinkList


class Node(object):

    def __init__(self, item):
        self.item = item

        # 双向链表指针
        self.next = None
        self.prev = None


class DoubleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):

        cur = self.__head
        count = 0

        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self.__head

        while cur != None:
            print(cur.item, end=",")
            cur = cur.next

    def add(self, item):
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):

        node = Node(item)
        cur = self.__head

        if self.is_empty():
            self.add(item)
        else:
            while cur.next != None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0

            while count < pos - 1:
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next.prev = node

            node.prev = pre
            pre.next = node

    def delete(self, item):
        '''

        :param item: item
        :return: True, deleted success, False, No have item, deleted failed.
        '''

        if self.is_empty():
            return False
        else:
            cur = self.__head
            if cur.item == item:
                if cur.next == None:
                    self.__head == None
                else:
                    self.__head = cur.next
                    cur.next.prev = None
                return
            else:
                while cur != None:
                    if cur.item == item:
                        cur.prev.next = cur.next
                        if cur.next:
                            cur.next.prev = cur.prev

                        print(f'Delete {cur.item} success.')
                        return True
                    else:
                        cur = cur.next
        print(f"Dont have this item {item}")
        return False

    def search(self, item):
        '''

        :param item: item
        :return: position
        '''
        cur = self.__head
        pos = 0
        while cur.next != None:
            if cur.item == item:
                print(f"Found this item {cur.item}, pos: {pos}")
                return pos
            else:
                pos += 1
                cur = cur.next
        return None
        print(f"Dont find this item {item}")


node1 = Node(100)
node2 = Node(200)
node1.next = node2
node2.prev = node1

link = DoubleLinkList(node1)

link.add(50)
link.add(40)
link.append(400)
link.append(300)
link.insert(3, 220)
link.insert(3, 210)
link.delete(10)
link.search(200)
link.delete(3000)
link.travel()

print(f"Length is {link.length()}")
# print(link.is_empty())
