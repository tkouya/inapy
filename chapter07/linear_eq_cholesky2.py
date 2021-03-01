# linear_eq_cholesky2.py: 問題7.4
import numpy as np
import scipy.linalg as slinalg
# 時間計測
import time

# 方法1 : Cholesky分解 + 前進後退代入
mat_a = np.array([[2, 1, -1], [1, 3, 1], [-1, 1, 4]])
vec_b = [2, 5, 4]
mat_chol, low = slinalg.cho_factor(mat_a)
vec_x = slinalg.cho_solve((mat_chol, low), vec_b) # x

print('x = ', vec_x)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
