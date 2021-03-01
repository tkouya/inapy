# ode_bvp_linear.py: ODE境界値問題(三重対角行列)
import numpy as np
import scipy.sparse as scsp
import scipy.sparse.linalg as scsplinalg


# Bulirsch & Stoer
def p(x):
    return 400 * x ** 0.0  # x毎に値を計算


def q(x):
    return 400 * (np.cos(np.pi * x)) ** 2 + 2 * np.pi ** 2 * np.cos(2 * np.pi * x)


def func(x, y):
    return p(x) * y + q(x)


# 真の解
def true_sol(x):
    return (np.exp(-20) / (1 + np.exp(-20))) * np.exp(20 * x) + (1 / (1 + np.exp(-20))) * np.exp(-20 * x) - (np.cos(np.pi * x)) ** 2


# [a, b] = [0, 1]
div = 501  # div : x方向分割数
# 境界条件
a, b = 0.0, 1.0
y_a, y_b = 0.0, 0.0

h = (b - a) / (div + 1)
x = np.linspace(a, b, div + 1)
in_x = x[1:div]  # 端点を除去

# 三重対角行列を生成
diag_element = -2.0 - p(in_x) * h ** 2
print('diag = ', diag_element)
bvp_mat = scsp.csr_matrix(scsp.spdiags(np.array([
    [ 1.0] * (div - 1),
    diag_element,
    [ 1.0] * (div - 1)
]), [-1, 0, 1], div - 1, div - 1))
print('bvp_mat = ', bvp_mat.toarray())

# 定数ベクトルを生成
bvp_vec = q(in_x)
bvp_vec[0] += -y_a
bvp_vec[-1] += -y_b
bvp_vec = (h ** 2) * bvp_vec
print('bvp_vec = ', bvp_vec)

# 直接法で解く
ret_y = scsplinalg.spsolve(bvp_mat, bvp_vec)

# 近似解の相対誤差を求める
true_y = true_sol(in_x)
relerr_y = np.abs(np.divide(ret_y - true_y, true_y))
print('div = ', div)
print('relerr = ', relerr_y)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
