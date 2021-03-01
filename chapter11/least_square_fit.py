# least_square_fit.py: 最小二乗法
import numpy as np
import scipy.optimize as scopt  # curve_fit
import scipy.stats as scsta  # linregres
import pandas as pd  # Pandas
import matplotlib.pyplot as plt


# 当て嵌め関数
def func(x, a0, a1):
    return a0 + a1 * x


# CSVファイル読み込み
data = pd.read_csv('./test_least_sq.csv')
print(data)

# 曲線当て嵌め: curve_fit
popt, pcov = scopt.curve_fit(func, data.iloc[:, 0], data.iloc[:, 1])
print('popt = ', popt)
print('pcov = ', pcov)

# 直線当て嵌め: linregress
ret = scsta.linregress(data.iloc[:, 0], data.iloc[:, 1])

# 結果確認
min_x = np.min(data.iloc[:, 0])
max_x = np.max(data.iloc[:, 0])
div_x = len(data.iloc[:, 0]) * 5  # 5倍の細かさ
h_x = (max_x - min_x) / div_x

print('        x                curve_fit                 linregress           reldiff')
for i in range(div_x + 1):
    x = min_x + h_x * i
    curve_fit_val = func(x, *popt)
    linregress_val = ret.intercept + ret.slope * x
    reldiff = np.abs((curve_fit_val - linregress_val) / (curve_fit_val))
    print(f'{x:15.5e}, {curve_fit_val:25.17e}, {linregress_val:25.17e}, {reldiff:10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
