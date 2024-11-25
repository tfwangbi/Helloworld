# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : socket_client.py
# Time       ：2024/5/21 15:39
# Author     ：author name
# version    ：python 3.6
# Description：
"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    re_data = input()
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode("utf8"))

    # client.close()