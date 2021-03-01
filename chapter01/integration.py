# integration.py: 定積分計算
import numpy as np


# 被積分関数
def func(x):
    return 5 * np.sqrt(1 - 0.8**2 * x**2) / np.sqrt(1 - x**2)


# 近似定積分
def integration(x_start, x_end, function, num_div):
    ret = 0
    h = (x_end - x_start) / num_div
    x = x_start
    x_next = x + h

    for i in range(0, num_div):
        ret += function((x + x_next) / 2) * h
        x = x_next
        x_next = x + h

    return ret


# 定積分
a, b, n = 0, 0.8, 100
print(f'integral[{a:f}, {b:f}] : {integration(a, b, func, n):25.17e}')

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
