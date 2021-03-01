# num_deriv.py: 前進・後退・中心差分商による数値微分
import numpy as np
from tktools import relerr  # 相対誤差


# 元の関数
def org_func(x):
    return np.sin(np.cos(x))


# 1階導関数
def diff_func(x):
    return np.cos(np.cos(x)) * (-np.sin(x))


# 前進差分商 : (func(x + h) - func(x)) / h
def forward_diff(func, x, h):
    return (func(x + h) - func(x)) / h


# 後退差分商 : (func(x) - func(x - h)) / h
def backward_diff(func, x, h):
    return (func(x) - func(x - h)) / h


# 中心差分商: (func(x + 0.5 * h) - func(x - 0.5 * h)) / h
def central_diff(func, x, h):
    return (func(x + 0.5 * h) - func(x - 0.5 * h)) / h


# 真の微分係数
x = np.pi / 4.0
true_deriv = diff_func(x)
print('真値                 = ', diff_func(x))

# 前進差分商，後退差分商，中心差分商
print('                      相対誤差                        ')
print('      h    　前進差分商  後退差分商  中心差分商')
for p in range(0, 10, 1):
    h = 10.0 ** (-p)  # 刻み幅

    fderiv = forward_diff(org_func, x, h)  # 前進差分商
    bderiv = backward_diff(org_func, x, h)  # 後退差分商
    cderiv = central_diff(org_func, x, h)  # 中心差分商

    print(f'{h:10.3e}, {relerr(fderiv, true_deriv):10.3e}, {relerr(bderiv, true_deriv):10.3e}, {relerr(cderiv, true_deriv):10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
