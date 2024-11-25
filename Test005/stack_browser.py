# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : stack_browser.py
# Time       ：2024/11/24 21:03
# Author     ：author name
# version    ：python 3.6
# Description：
"""


from stack import Stack

class Browser(object):

    def __init__(self):

        self.x = Stack()
        self.y = Stack()

    def back(self):
        # self.y.push(self.x.peek())

        if self.x.is_empty():
            return

        top = self.x.pop()
        self.y.push(top)

        print(f"Back to {self.x.peek()}")

    def forward(self):
        # pass
        if self.y.is_empty():
            return

        top = self.y.pop()
        # print(top)
        self.x.push(top)

        print(f"Forward to {self.x.peek()}")

    def open(self, url):
        print(f"Open url: {url}")
        self.x.push(url)

    def can_back(self):
        if self.x.is_empty():
            return False
        return True

    def can_forward(self):
        if self.y.is_empty():
            return False
        return True

if __name__ == "__main__":

    b = Browser()
    b.open("url1")
    b.open("url2")
    b.open("url3")
    b.open("url4")

    if b.can_back():
        b.back()
        b.back()

    if b.can_forward():
        b.forward()