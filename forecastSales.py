# -*- coding: utf-8 -*-
"""Forecast.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DA3eXwiUwR1aC2CfpWDUMGRKVhDcR3sY
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from datetime import datetime, timedelta

dataset = pd.read_csv('TotalSales.csv')

y = dataset['Sum of LineTotal']
X = dataset.iloc[:,0:4]

Quarter = X['Quarter']

newQuarter = []
for qtr in Quarter:
    newQuarter.append(qtr[4:5])

del X['Quarter']

X.insert(1, 'Quarter', newQuarter)

monthConv = {'January': 1,'February': 2,'March': 3,'April': 4,'May': 5,'June': 6,
    'July': 7,'August': 8,'September': 9,'October': 10,'November': 11,'December': 12
}

Month = X['Month']

newMonth = []
for month in Month:
  newMonth.append(monthConv[month])

del X['Month']

X.insert(1, 'Month', newMonth)

print(X['Quarter'])

import pandas as pd

# Generating days for Quarter 3 (months 7, 8, 9) and Quarter 4 (months 10, 11, 12) of 2014
quarter_3_days = pd.date_range(start='2014-07-01', end='2014-09-30')
quarter_4_days = pd.date_range(start='2014-10-01', end='2014-12-31')

# Creating DataFrames for Quarter 3 and Quarter 4 days
quarter_3_df = pd.DataFrame({
    'Year': quarter_3_days.year,
    'Month': quarter_3_days.month,
    'Quarter': ((quarter_3_days.month - 1) // 3) + 1,  # Calculate the quarter based on month
    'Day': quarter_3_days.day
})

quarter_4_df = pd.DataFrame({
    'Year': quarter_4_days.year,
    'Month': quarter_4_days.month,
    'Quarter': ((quarter_4_days.month - 1) // 3) + 1,  # Calculate the quarter based on month
    'Day': quarter_4_days.day
})

# Displaying Quarter 3 and Quarter 4 DataFrames

predictionPeriod = quarter_3_df.append(quarter_4_df, ignore_index=True)

print(predictionPeriod)

newY = []
for t_y in y:
    newY.append(t_y[1:-1])

print(newY)

lin = LinearRegression()
lin.fit(X, newY)
y_pred = lin.predict(predictionPeriod)

# prediction = []
# for t_y in y_pred:
#   prediction

prediction = np.round(y_pred, 2)

# print(prediction)

predictionPeriod.insert(4,"prediction", prediction);
print(predictionPeriod)

predictionPeriod.to_excel('Forecast.xlsx')

2014*10000+7*100+31