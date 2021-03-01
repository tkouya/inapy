# eig.py: 行列の固有値と固有ベクトル
import numpy as np
import scipy.linalg as sclinalg

# 行列を与える
mat_a = np.array([[2, 2], [1, 1]])

# 行列確認
print('A = \n', mat_a)

# 固有値と固有ベクトル
eigval, ev = sclinalg.eig(mat_a)
ev = ev.T  # 転置
print('Eigenvalues = ', eigval)
print('Eigenvectors = \n', ev)

# 検算 ||A * v - lambda * v|| == 0 ?
for i in range(0, eigval.size):
    print(
        '|| A * v - lambda[', i, '] * v||_2 = ',
        sclinalg.norm(mat_a @ ev[i] - eigval[i] * ev[i])
    )


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
