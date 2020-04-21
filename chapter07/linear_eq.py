# linear_eq.py: 連立一次方程式を解く方法
import numpy as np
import scipy as spy
import scipy.linalg as slinalg
# 時間計測
import time

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# 乱数行列をAとして与える
np.random.seed(20190514)
mat_a = spy.random.rand(dim, dim)
#print(mat_a)

# x = [1 2 ... dim]
vec_true_x = spy.arange(1, dim + 1)
#print(vec_true_x)

# b = A * x
vec_b = mat_a @ vec_true_x

# 方法1 : 逆行列A^(-1)を求めて x := A^(-1) * bとする
start_time = time.time()
inv_mat_a = slinalg.inv(mat_a) # A^(-1)
vec_x = inv_mat_a @ vec_b      # A^(-1) * b
time1  = time.time() - start_time

relerr1 = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('time = ', time1, ', relerr(vec_x) = ', relerr1)

# 方法2 : solve関数を使う
start_time = time.time()
vec_x = slinalg.solve(mat_a, vec_b) # x
time2  = time.time() - start_time

relerr2 = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('time = ', time2, ', relerr(vec_x) = ', relerr2)

# 方法3 : lu分解 + 前進後退代入
start_time = time.time()
mat_lu, pivot = slinalg.lu_factor(mat_a) # PLU = A
vec_x = slinalg.lu_solve((mat_lu, pivot), vec_b)
time3  = time.time() - start_time

relerr3 = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('time = ', time3, ', relerr(vec_x) = ', relerr3)

