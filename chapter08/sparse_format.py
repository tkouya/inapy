# sparse_format.py: 疎行列フォーマット
import numpy as np
import scipy.sparse as scsp  # SciPy.sparse

# 密行列
mat_a = np.array([
    [1, 0, 2, 0, 0],
    [0, 3, 0, 0, -4],
    [0, 0, 5, 0, 0],
    [6, 0, 0, -7, 0],
    [0, 0, 0, 0, 8]
])
print('A = \n', mat_a)

# COO形式
spmat_a_coo = scsp.coo_matrix(mat_a)
print('COO A = \n', spmat_a_coo)

# CSR形式
spmat_a_csr = scsp.csr_matrix(mat_a)
print('CSR A = \n', spmat_a_csr)

# CSC形式
spmat_a_csc = scsp.csc_matrix(mat_a)
print('CSC A = \n', spmat_a_csc)

# 密行列に戻す
print('CSR -> Dense: \n', spmat_a_csr.todense())
print('CSC -> Dense: \n', spmat_a_csc.todense())


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
