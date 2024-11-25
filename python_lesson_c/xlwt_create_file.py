# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : xlwt_create_file.py
# Time       ：2024/5/14 14:30
# Author     ：author name
# version    ：python 3.6
# Description：
"""

import xlwt

local = r'../../files/excel/'

# create excel
wb = xlwt.Workbook()
# 选择工作簿
sh = wb.add_sheet('电影')
# 写数据到单元格 (0, 0)
sh.write(2,6, 'Test data')
# 保存excel
wb.save(f'{local}电影数据.xls')
