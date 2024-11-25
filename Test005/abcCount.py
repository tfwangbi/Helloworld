# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : abcCount.py
# Time       ：2024/11/23 14:28
# Author     ：author name
# version    ：python 3.6
# Description：
"""

import time
from timeit import Timer

start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#
#             if a**2 + b**2 == c**2 and a + b + c == 1000:
#                 print(f'a, b, c: {a}, {b}, {c}')


for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f'a, b, c: {a}, {b}, {c}')

end_time = time.time()

print(f'times: {(end_time-start_time)}')