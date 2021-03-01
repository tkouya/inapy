# interpol.py: 多項式補間
import numpy as np
import scipy.linalg as sclinalg
import scipy.interpolate as scipl


# 大本の関数
def org_func(x):
    return np.sin(x)


# 補間点数
str_n = input('補間点数を入力 n = ')
n = int(str_n)

# 補間点
x = np.zeros(n)
y = np.zeros(n)
print('x.size = ', x.size)
for i in range(0, n):
    print('補間点xを入力 x[' + str(i) + '] = ')
    str_x = input()
    x[i] = float(str_x)
    y[i] = org_func(x[i])

print('x = ', x)
print('y = ', y)

# バンデルモンド行列生成
v_mat = np.zeros((n, n))
for i in range(0, n):
    for j in range(0, n):
        v_mat[i, j] = x[i] ** j

print('V = \n', v_mat)

# new_y := V^(^1) * y
v_coef = sclinalg.inv(v_mat) @ y
print('v_coef = ', np.flip(v_coef))

# ラグランジュ補間
l_poly = scipl.lagrange(x, y)
print('l_coef = ', l_poly.coef)

# Kroph補間
k_poly = scipl.KroghInterpolator(x, y)
print('k(x) = ', k_poly(x))
print('k\'(x) = ', k_poly.derivative(x, der=1))
print('k\'\'(x) = ', k_poly.derivative(x, der=2))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
