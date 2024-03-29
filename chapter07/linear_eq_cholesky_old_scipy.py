# linear_eq_cholesky.py: 連立一次方程式を解く(正定値対称行列)
import numpy as np
import scipy as sc
import scipy.linalg as sclinalg
# 時間計測
import time

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# 対称乱数行列をAとして与える
np.random.seed(20200529)
mat_a1 = sc.random.rand(dim, dim)
# 正定値対称化: A = A1 * A1^T
mat_a = mat_a1 @ mat_a1.T

# x = [1 2 ... dim]
vec_true_x = np.arange(1, dim + 1)

# b = A * x
vec_b = mat_a @ vec_true_x

# 方法1 : Cholesky分解 + 前進後退代入
start_time = time.time()
mat_chol, low = sclinalg.cho_factor(mat_a)
vec_x = sclinalg.cho_solve((mat_chol, low), vec_b)  # x
time2 = time.time() - start_time

relerr2 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'Cholesky(seconds) = {time2:5.2g}, relerr(vec_x) = {relerr2:10.3e}')

# 方法2 : LDT^T分解 + 前進後退代入
start_time = time.time()
mat_l, mat_d, perm = sclinalg.ldl(mat_a)  # LDL分解
mat_l = mat_l[perm, :]   # 行入れ替えを修正
ldl_vec_b = vec_b[perm]  # 同上

vec_y = sclinalg.solve_triangular(
    mat_l, ldl_vec_b, lower=True, trans=0, unit_diagonal=True
)  # Ly = b
vec_z = [vec_y[i] / mat_d[i, i] for i in range(dim)]  # Dz = y
vec_x = sclinalg.solve_triangular(
    mat_l, vec_z, lower=True, trans=1, unit_diagonal=True
)  # L^T x = z
time2 = time.time() - start_time

relerr2 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'LDL^T(seconds)    = {time2:5.2g}, relerr(vec_x) = {relerr2:10.3e}')

# 方法3 : lu分解 + 前進後退代入
start_time = time.time()
mat_lu, pivot = sclinalg.lu_factor(mat_a)  # PLU = A
vec_x = sclinalg.lu_solve((mat_lu, pivot), vec_b)
time3 = time.time() - start_time

relerr3 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'LU(seconds)       = {time3:5.2g}, relerr(vec_x) = {relerr3:10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
