# lu2.py: 問題7.2
import numpy as np
import scipy.linalg as slinalg

mat_a = np.array([[2, 1, -1], [1, 3, 1], [-1, 1, 4]])
vec_b = np.array([3, 20, 33])

# LU分解(2)
LU, pivot = slinalg.lu_factor(mat_a)
print('Pivot = ', pivot)
print('LU = \n', LU)

# LU分解から前進・後退代入
x = slinalg.lu_solve((LU, pivot), vec_b)
print('x = ', x)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
