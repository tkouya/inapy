# deriv.py: 数値微分
import scipy.misc as scmisc
import numpy as np
from tktools import relerr  # 相対誤差


# 中央差分式の係数(奇数点数のみ)を出力
for m in range(1, 6):
    print('--- ', m, '階差分 ---')
    if m >= 3:
        min_num_points = 2 * m - 1
    else:
        min_num_points = 3
    for n in range(min_num_points, 10, 2):
        print(n, '点公式: ', scmisc.central_diff_weights(n, m))


# 元の関数
def org_func(x):
    return np.sin(np.cos(x))


# 1階導関数
def diff_func(x):
    return np.cos(np.cos(x)) * (-np.sin(x))


# 中心差分商に基づく数値微分
x = 1.5
print('真値                 = ', diff_func(x))

approx_diff = scmisc.derivative(org_func, x)
print(f'中央差分商   標準設定: {approx_diff:25.17e} {relerr(approx_diff, diff_func(x)):10.3e}')

n = 3
dx = 0.1
approx_diff = scmisc.derivative(org_func, x, dx, order=n)
print(f'中央差分商 {n:3d}点公式 : {approx_diff:25.17e} {relerr(approx_diff, diff_func(x)):10.3e}')

n = 5
dx = 0.1
approx_diff = scmisc.derivative(org_func, x, dx, order=n)
print(f'中央差分商 {n:3d}点公式 : {approx_diff:25.17e} {relerr(approx_diff, diff_func(x)):10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
