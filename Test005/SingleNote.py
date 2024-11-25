# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : SingleNote.py
# Time       ：2024/11/24 12:36
# Author     ：author name
# version    ：python 3.6
# Description：
"""


class SingleNote(object):
    def __init__(self, item):
        self.item = item
        # next note
        self.next = None


class SingleLinkList(object):

    def __init__(self, node=None):
        # 头部域 空链表 = None
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
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

        # 添加到最后一位
        note = SingleNote(item)

        if self.is_empty():
            self.__head = note
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next

            cur.next = note

    def add(self, item):

        note = SingleNote(item)
        note.next = self.__head
        self.__head = note

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            note = SingleNote(item)
            pre = self.__head
            count = 0

            while count < pos - 1:
                cur = pre.next
                count += 1

            note.next = pre.next
            pre.next = note

    def remove(self, item):
        pre = None
        cur = self.__head

        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next

                print('Delete success.')
                return
            else:
                pre = cur
                cur = cur.next

    def search(self, item):

        cur = self.__head
        count = 0

        while cur.next != None:
            if cur.item == item:
                print(f"search success. pos:{count}")
                return True
            else:
                cur = cur.next
                count += 1

        print(f"Don't have this item ({item}) in the link")


if __name__ == '__main__':
    note1 = SingleNote(10)
    note2 = SingleNote(20)
    note3 = SingleNote(30)
    note4 = SingleNote(40)

    note1.next = note2
    note2.next = note3
    note3.next = note4

    # print(note1.next.item)

    link = SingleLinkList(note1)
    link.append(50)
    link.add(5)
    link.insert(3, 120)
    link.insert(-2, 3)

    link.travel()

    link.search(100)

    # print(link.length())
