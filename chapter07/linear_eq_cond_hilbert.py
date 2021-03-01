# linear_eq_cond_hilbert.py: 連立一次方程式と条件数
import numpy as np
import scipy.linalg as sclinalg

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# ヒルベルト行列
mat_a = sclinalg.hilbert(dim)

# x = [1 2 ... dim]
vec_true_x = np.arange(1, dim + 1)

# b = A * x
vec_b = mat_a @ vec_true_x

# lu分解 + 前進後退代入
mat_lu, pivot = sclinalg.lu_factor(mat_a)  # PLU = A
vec_x = sclinalg.lu_solve((mat_lu, pivot), vec_b)

relerr3 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'relerr(vec_x) = {relerr3:10.3e}')

# Aの条件数を求める
print(f'cond(mat_a)                    = {np.linalg.cond(mat_a):10.3e}')
print(f'||mat_a||_2 * ||mat_a^(-1)||_2 = {sclinalg.norm(mat_a) * sclinalg.norm(sclinalg.inv(mat_a)):10.3e}')
print(f'cond(mat_a, 1)                 = {np.linalg.cond(mat_a, 1):10.3e}')
print(f'||mat_a||_1 * ||mat_a^(-1)||_1 = {sclinalg.norm(mat_a, 1) * sclinalg.norm(sclinalg.inv(mat_a, 1)):10.3e}')
print(f'cond(mat_a, inf)               = {np.linalg.cond(mat_a, np.inf):10.3e}')
print(f'||mat_a||_i * ||mat_a^(-1)||_i = {sclinalg.norm(mat_a, np.inf) * sclinalg.norm(sclinalg.inv(mat_a), np.inf):10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
