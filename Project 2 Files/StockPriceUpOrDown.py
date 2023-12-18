# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:14:13 2023

@author: frie1379
"""

import pandas as pd

df = pd.read_csv('AMZN_Price_Last_5_Years.csv')
df = df.reset_index()



for i in range(0, len(df)-1):
    close = df.iloc[i]['Close/Last']
    prevClose = df.iloc[i + 1]['Close/Last']
    if(float(close[1:len(close)]) >= float(prevClose[1:len(close)])):
        df['Price Increase'][i] = "Yes"
        df['Previous Close'][i] = prevClose
    else:
        df['Price Increase'][i] = "No"
        df['Previous Close'][i] = prevClose
        
df.to_csv('AMZN_Price_Last_5_Years.csv', mode='w', index = False)

