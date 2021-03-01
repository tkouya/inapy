# basic_matrix.py: 行列の基本演算
import numpy as np

# 行列の定義
mat_a = np.array([[1, 2, 3], [2, 2, 3], [3, 3, 3]])
print('A = \n', mat_a)
mat_b = np.array([[-3, -3, -3], [-3, -2, -2], [-3, -2, -1]])
print('B = \n', mat_b)

# ベクトルの定義
vec_x = np.array([1, 2, 3])
print('x = ', vec_x)

# BLAS Level2
# 行列，ベクトル演算: 行列・ベクトル積
mat_ax = mat_a.dot(vec_x)
print('Ax = ', mat_ax)

# 3A - 4B
mat_3am4b = 3 * mat_a - 4 * mat_b
print('3A - 4B = \n', mat_3am4b)

# BLAS Level3
# 行列演算: 行列積
mat_ab = mat_a.dot(mat_b)  # 方法1
print('A * B = \n', mat_ab)
mat_ab_at = mat_a @ mat_b  # 方法2
print('A @ B = \n', mat_ab_at)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------