# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : pandas_lesson_1.py
# Time       ：2024/4/23 14:20
# Author     ：author name
# version    ：python 3.6
# Description：
"""
import pandas as pd

local = r'../../files/datas/'
# fpath_csv = 'gen_strings_schinese.csv'
fpath_csv = 'test_weather.csv'
fpath_txt = 'weather_test.txt'

if __name__ == '__main__':

    df = pd.read_csv(local+fpath_csv, encoding='utf-8')
    # ['Date', 'Out T.(ºC)', 'Out H.(%)', 'Wind Dir.', 'W.Sp.(km/h)', 'SLP(hpa)', 'Int.T.(ºC)', 'Prec.(mm/h)']
    # print(df.head())
    # print(df[['Date']])
    df.set_index('Date', inplace=True)

    # print(df.index)
    # print(df.head())
    # print(df.loc[:, 'Out T.(ºC)'])
    df.loc[:, 'Out T.(ºC)'] = df['Out T.(ºC)'].str[:4]
    print(df.head())
