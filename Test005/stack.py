# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : stack.py
# Time       ：2024/11/24 20:49
# Author     ：author name
# version    ：python 3.6
# Description：
"""

class Stack(object):

    '''
    create a new empty stack
    '''
    def __init__(self):

        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        '''

        :return:
        '''
        return self.__items.pop()

    def peek(self):

        if self.__items:
            # return self.__items.pop()
            return self.__items[len(self.__items)-1]
        else:
            return None
    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(0)

    s.pop()
    print(s.peek())