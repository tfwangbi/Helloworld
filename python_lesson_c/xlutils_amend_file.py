# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : xlutils_amend_file.py
# Time       ：2024/5/14 16:03
# Author     ：author name
# version    ：python 3.6
# Description：
"""
from xlutils.copy import copy
import xlrd

local = r'../../files/excel/'

read_book = xlrd.open_workbook(f'{local}电影数据.xls')

# sh1 = read_book.sheet_by_index(0)
# print(sh1.ncols)
# copy data
wb = copy(read_book)
sh = wb.get_sheet(0)
sh.write(2,2, 'bbb')
sh.write(2,3, 'ccc')

sh2 = wb.add_sheet('电影1')

# print(sh.)


