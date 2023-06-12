# inv.py: 逆行列を求める
import numpy as np
import scipy as sc
import scipy.linalg as sclinalg

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# 乱数行列をAとして与える
np.random.seed(20200529)
mat_a = sc.random.rand(dim, dim)
print('A = \n', mat_a)

# 乱数ベクトルをtrue_xとする
true_x = sc.random.rand(dim)

# 逆行列を求める
mat_a_inv = sclinalg.inv(mat_a)
print('A^(-1) = \n', mat_a_inv)
# print('|| A * A^(-1) - I|| == 0? ->', np.linalg.norm(mat_a @ mat_a_inv - sc.eye(dim)))  # SciPy 2.0.0以上でWarning
print('|| A * A^(-1) - I|| == 0? ->', np.linalg.norm(mat_a @ mat_a_inv - np.eye(dim)))  # NumPy.eyeを使用

# 連立一次方程式 Ax = bを解く
b = mat_a @ true_x

# x := A^(-1) * b
x = mat_a_inv @ b
print('x = ', x)
print(f'rE(x) = {np.linalg.norm(true_x - x) / np.linalg.norm(true_x):10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
