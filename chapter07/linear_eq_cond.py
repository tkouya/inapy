# linear_eq_cond.py: 連立一次方程式と条件数
import numpy as np
import scipy as spy
import scipy.linalg as slinalg

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# 乱数行列をAとして与える
# np.random.seed(20190514)
# mat_a = spy.random.rand(dim, dim)

# Hilbert行列
mat_a = slinalg.hilbert(dim)

# x = [1 2 ... dim]
vec_true_x = spy.arange(1, dim + 1)

# b = A * x
vec_b = mat_a @ vec_true_x

# lu分解 + 前進後退代入
mat_lu, pivot = slinalg.lu_factor(mat_a) # PLU = A
vec_x = slinalg.lu_solve((mat_lu, pivot), vec_b)

relerr3 = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('relerr(vec_x) = ', relerr3)

# Aの条件数を求める
print('cond(mat_a)                  = ', np.linalg.cond(mat_a))
print('||mat_a||_2 * ||mat_a^(-1)|| = ', slinalg.norm(mat_a) * slinalg.norm(slinalg.inv(mat_a)))
