# newton_mdim.py: 多次元ニュートン法
import numpy as np
import scipy.optimize as scopt


# f(x) = 0
def func(x):
    return [x[0] + x[1] - 3, x[0] * x[1] - 2]


# f'(x) = 0
def dfunc(x):
    return np.array([
        [1, 1],
        [x[1], x[0]]
    ])


# 初期値
x0 = [10, -10]

# root関数(1)
final = scopt.root(func, x0)

# 表示
print('----- root関数(1) -----\n', final)
print('最終 -> x =')
for i in range(0, (final.x).size):
    print(f'{i:3d}, {final.x[i]:25.17e}')

print('検算 -> f(x) = ')
for i in range(0, (final.fun).size):
    print(f'{i:3d}, {final.fun[i]:25.17e}')

# root関数(2)
final = scopt.root(func, x0, jac=dfunc)

# 表示
print('----- root関数(2) -----\n', final)
print('最終 -> x =')
for i in range(0, (final.x).size):
    print(f'{i:3d}, {final.x[i]:25.17e}')

print('検算 -> f(x) = ')
for i in range(0, (final.fun).size):
    print(f'{i:3d}, {final.fun[i]:25.17e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
