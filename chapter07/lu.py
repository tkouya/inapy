# lu.py: LU分解
import numpy as np
import scipy as sc
import scipy.linalg as sclinalg

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# 乱数行列をAとして与える
np.random.seed(20200529)
mat_a = np.random.rand(dim, dim)
print('A = \n', mat_a)

# 乱数ベクトルをtrue_xとする
true_x = np.random.rand(dim)

# LU分解(1)
P, L, U = sclinalg.lu(mat_a)  # PLU = A

print('P = \n', P)
print('L = \n', L)
print('U = \n', U)

print('|| P * L * U - A|| == 0? ->', np.linalg.norm(P @ L @ U - mat_a) / np.linalg.norm(mat_a))

# LU分解(2)
LU, pivot = sclinalg.lu_factor(mat_a)
print('Pivot = ', pivot)
print('LU = ', LU)

# 連立一次方程式 Ax = bを解く
b = mat_a @ true_x

# LU分解から前進・後退代入
x = sclinalg.lu_solve((LU, pivot), b)
print('x = ', x)
print(f'rE(x) = {np.linalg.norm(true_x - x) / np.linalg.norm(true_x):10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
