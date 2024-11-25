# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : excel_lesson_2.py
# Time       ：2024/4/11 14:07
# Author     ：author name
# version    ：python 3.6
# Description：
"""
import pandas as pd
import xlrd
import xlwt

local = r'../../files/excel/'

if __name__ == '__main__':

    # List to create dataFrame
    data = [['Apple', '35.5', '100'], ['Orange', '25', '50'], ['Banana', '31', '66']]
    columns = ['Name', 'Unit', 'Pricing']
    df = pd.DataFrame(data=data, columns=columns)

    # print(df)

    # Dict to create dataFrame

    data_2 = {
        'Name': ['Apple', 'Orange', 'Banana'],
        'Unit': [35.5, 35, ''],
        'Pricing': [100, 50, 66],
        'Location': 'XIAN'
    }

    df2 = pd.DataFrame(data=data_2)
    # print(df2.head(2))
    # print(df2.tail(2))

    # print(df2.values)
    # print(df2.index)  # Row index
    # print(df2.columns)
    # df2.columns = ['AName', 'BUnit', 'CPricing', 'DLocation']
    # print(df2.columns)
    # new_df = df2.T
    # print(new_df)
    # print(df2.shape, df2.info)

    print(df[['Name', 'Pricing']])
    print(df.loc[0:3])

