# eig2.py: 演習問題２
import numpy as np
import scipy.linalg as slinalg

# 行列を与える
mat_a = np.array([[1, -2], [-2, 3]])  # A1
#mat_a = np.array([[1, -2], [0, 3]])  # A2
#mat_a = np.array([[1, 0], [-2, 3]])  # A3

# 行列確認
print('A = \n', mat_a)

# 固有値と固有ベクトル
eigval, ev = slinalg.eig(mat_a)
ev = ev.T # 転置
print('Eigenvalues = ', eigval)
print('Eigenvectors = \n', ev)

# 検算 ||A * v - lambda * v|| == 0 ?
for i in range(0, eigval.size) :
	print('|| A * v - lambda[', i, '] * v||_2 = ', slinalg.norm(mat_a @ ev[i] - eigval[i] * ev[i]))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
