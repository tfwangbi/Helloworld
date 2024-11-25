# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : single_link_list.py
# Time       ：2024/11/23 19:01
# Author     ：author name
# version    ：python 3.6
# Description：单链表的实现和操作
"""


# 节点实现
class SingleNode(object):
    def __init__(self, item):
        self.item = item
        # 下一个节点的标识
        self.next = None


node1 = SingleNode(100)
node2 = SingleNode(200)
node3 = SingleNode(300)
node4 = SingleNode(400)

node1.next = node2
node2.next = node3
node3.next = node4


# print(node1.next.item)
# print(node2.next.item)


# 链表实现
class SingleLinkList(object):

    def __init__(self, node=None):
        # pass
        # 空链表
        # self.__head = None
        self.__head = node

    def is_empty(self):
        # if self.__head == None:
        #         #     return True
        #         # else:
        #         #     return False
        return self.__head == None;

    def length(self):
        count = 0
        cur = self.__head

        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def append(self, item):
        node = SingleNode(item)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next

            cur.next = node

    def add(self, item):

        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        '''
        :param pos: 下标
        :param item: 添加的元素
        :return:
        '''
        if pos < 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next

        return False

    def delete(self, item):

        cur = self.__head
        pre = None

        while cur != None:
            if cur.item == item:

                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next

                print("Delete success.")
                return
            else:
                pre = cur
                cur = cur.next

        print("Don't have this item.")


s = SingleLinkList(node1)
s.append(500)
s.append(600)
s.add(90)
s.insert(-1, 250)
# print(s.length())
s.travel()
s.delete(100)
print("-----delete------")
s.travel()
