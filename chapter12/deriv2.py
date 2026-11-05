# deriv2.py: 問題12.2
import numpy as np
import findiff # findiff # 数値微分パッケージ
from tktools import relerr  # 相対誤差


# 元の関数
def org_func(x):
    # return np.sin(np.cos(x))
    return np.exp(np.sin(x))


# 1階導関数
def diff_func(x):
    # return np.cos(np.cos(x)) * (-np.sin(x))
    return np.exp(np.sin(x)) * np.cos(x)

# 2階導関数
def diff2_func(x):
    # return -np.sin(np.cos(x)) * (-np.sin(x))**2 + (np.cos(np.cos(x)) * (-np.cos(x)))
    return np.exp(np.sin(x)) * (np.cos(x) ** 2 - np.sin(x))

# 中心差分商に基づく数値微分
x = np.linspace(0, 1, 10)
print('真値                 = ', diff_func(x))

# 1階導関数
print('-- First derivative --')
for n in range(2, 6, 2):
    print('n = ', n)
    dx = x[1] - x[0]
    # 1階導関数の数値微分
    approx_diff_func = findiff.Diff(0, dx, acc=n)
    org_func_val = org_func(x)
    approx_diff = approx_diff_func(org_func_val)
    #        x             f'(x)           num.deriv      relerr
    #  0.0000000e+00,  -0.0000000e+00,   6.6622932e-04,  6.662e-04
    print('        x             f\'(x)           num.deriv      relerr ')
    for i in range(len(approx_diff)):
        print(f'{x[i]:15.7e}, {diff_func(x[i]):15.7e}, {approx_diff[i]:15.7e}, {relerr(approx_diff[i], diff_func(x[i])):9.2e}')

# 2階導関数
print('-- Second derivative --')
for n in range(2, 6, 2):
    print('n = ', n)
    dx = x[1] - x[0]
    # 2階導関数の数値微分
    approx_diff_func = findiff.Diff(0, dx, acc=n)**2
    org_func_val = org_func(x)
    approx_diff = approx_diff_func(org_func_val)
    print('        x             f\'\'(x)          num.deriv      relerr ')
    for i in range(len(approx_diff)):
        print(f'{x[i]:15.7e}, {diff2_func(x[i]):15.7e}, {approx_diff[i]:15.7e}, {relerr(approx_diff[i], diff2_func(x[i])):9.2e}')


# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------

