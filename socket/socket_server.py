# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : socket_server.py
# Time       ：2024/5/21 15:39
# Author     ：author name
# version    ：python 3.6
# Description：
"""

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)

        print(data.decode("utf8"))
        if data.decode("utf8") == 'exit':
            print('connecting is shut down')
            break
        re_data = input()
        sock.send(re_data.encode('utf8'))
    sock.close()


while True:
    sock, addr = server.accept()

    # 多线程
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024)
    # print(data.decode('utf8'))
    # re_data = input()
    # sock.send(re_data.encode('utf8'))

    # server.close()
    # sock.close()
