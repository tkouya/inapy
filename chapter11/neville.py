# neville.py: Newton補間・Nevilleのアルゴリズム
import numpy as np


# 元の関数
def org_func(x):
    return 1.0 / (25.0 + x ** 2)


# Nevilleのアルゴリズム
# 補間多項式を返す
def neville_interpoly(x, y):
    dim = len(x)
    if len(y) != dim:
        print('len(y) is not the same of len(x)!')
        return 0

    old_poly = [np.poly1d([0.0, y[i]]) for i in range(dim)]
    new_poly = old_poly[:]  # 初期化
    for j in range(1, dim):
        for i in range(j, dim):
            new_poly[i] = (np.poly1d([1.0, -x[i - j]]) * old_poly[i] - np.poly1d([1.0, -x[i]]) * old_poly[i - 1]) / (x[i] - x[i - j])
            print(i, j, '\n', new_poly[i])

        old_poly = new_poly[:]

    return new_poly[dim - 1]


# 補間点を生成
div_x = 5
x_min, x_max = -5.0, 5.0

x = np.linspace(x_min, x_max, div_x)
y = org_func(x)

print('x = ', x)
print('y = ', y)

interpoly = neville_interpoly(x, y)
print('Interpoly:\n', interpoly)
print('y            = ', x)
print('interpoly(x) = ', interpoly(x))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
