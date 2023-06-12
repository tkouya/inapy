# linear_eq.py: 連立一次方程式を解く方法
import numpy as np
import scipy as sc
import scipy.linalg as sclinalg
# 時間計測
import time

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# 乱数行列をAとして与える
np.random.seed(20200529)
mat_a = sc.random.rand(dim, dim)

# x = [1 2 ... dim]
vec_true_x = np.arange(1, dim + 1)

# b = A * x
vec_b = mat_a @ vec_true_x

# 方法1 : 逆行列A^(-1)を求めて x := A^(-1) * bとする
start_time = time.time()
inv_mat_a = sclinalg.inv(mat_a)  # A^(-1)
vec_x = inv_mat_a @ vec_b        # A^(-1) * b
time1 = time.time() - start_time

relerr1 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'time = {time1:10.3g}, relerr(vec_x) = {relerr1:10.3e}')

# 方法2 : solve関数を使う
start_time = time.time()
vec_x = sclinalg.solve(mat_a, vec_b)  # x
time2 = time.time() - start_time

relerr2 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'time = {time2:10.3g}, relerr(vec_x) = {relerr2:10.3e}')

# 方法3 : lu分解 + 前進後退代入
start_time = time.time()
mat_lu, pivot = sclinalg.lu_factor(mat_a)  # PLU = A
vec_x = sclinalg.lu_solve((mat_lu, pivot), vec_b)
time3 = time.time() - start_time

relerr3 = sclinalg.norm(vec_x - vec_true_x) / sclinalg.norm(vec_true_x)
print(f'time = {time3:10.3g}, relerr(vec_x) = {relerr3:10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
