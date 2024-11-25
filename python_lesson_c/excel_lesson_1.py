# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : excel_lesson_1.py
# Time       ：2024/4/9 10:26
# Author     ：author name
# version    ：python 3.6
# Description：
"""

import pandas as pd
import numpy as np
import openpyxl as xl
import xlrd
import xlwt
import os


class HandleExcel:
    def __init__(self, path):
        self.path = path

    def read_file(self):
        # return xl.load_workbook(self.path)
        return pd.read_excel(self.path, sheet_name=0, header=2, index_col=0)

    def save_to_file(self, data):
        df = pd.DataFrame(data)
        if os.path.exists(self.path):
            with pd.ExcelWriter(self.path, mode='a') as writer:
                df.to_excel(writer, sheet_name='temp_table', index=False)
        else:
            raise FileNotFoundError


if __name__ == '__main__':
    local = r'../../files/excel/'
    path = fr'{local}monthly_data.xlsx'
    passenger_path = fr'{local}passenger volume_monthly.xlsx'

    xls = HandleExcel(passenger_path)
    wb = xls.read_file()

    # data = wb.head(20)

    # print(type(wb))
    # print(wb.head(9))
    # print(wb.index)
    # print(wb.columns)
    # print(wb.columns.values)
    # print(wb['2023年11月'].values)
    # print(data)

    # data = {'One': [1, 2, 3]}
    # xls.save_to_file(data)

    # print(wb.columns.values)
    #
    # for ch in wb.sample(20):
    #     # print(ch)
    #     print(wb[ch])

    # pd.Series()
