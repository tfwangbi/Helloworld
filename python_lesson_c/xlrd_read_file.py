# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : xlrd_read_file.py
# Time       ：2024/5/14 14:45
# Author     ：author name
# version    ：python 3.6
# Description：
"""

import xlrd

local = r'../../files/excel/'

wb = xlrd.open_workbook(f'{local}月度数据.xls')
print(wb.nsheets)
print(wb.sheet_names())

sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_name('月度数据')

print(f'Rows: {sh1.nrows}, Cols: {sh1.ncols}')
print(f'单元格数据:{sh1.row(4)[1].value}')
print(f'单元格数据:{sh1.cell(4,1).value}')
print(f'单元格数据:{sh2.cell_value(4,1)}')

# for item in sh1.row(4):
#     print(item.value)

# 获取整行整列数据

print(sh1.row_values(2))

# all data

for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'{r+1}行，{c+1}列的数据是:{sh1.cell(r,c).value}')