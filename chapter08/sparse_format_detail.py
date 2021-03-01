# sparse_format_detail.py: 疎行列フォーマット
import numpy as np
import scipy.sparse as scsp

# A = [1 0 2 0  0]
#     [0 3 0 0 -4]
#     [0 0 5 0  0]
#     [6 0 0 -7 0]
#     [0 0 0 0  8]

# 密行列(1)
mat_a = np.array([
	[1, 0, 2, 0, 0],
	[0, 3, 0, 0, -4],
	[0, 0, 5, 0, 0],
	[6, 0, 0, -7, 0],
	[0, 0, 0, 0, 8]
])
# 密行列(2)
mat_a = np.array([
	[4, 0, 3],
	[0, 2, 0],
	[0, 0, 1]
])
print('A = \n', mat_a)
print('A : ')
print('dtype = ', mat_a.dtype)
print('shape = ', mat_a.shape)
print('ndim  = ', mat_a.ndim)
print('size  = ', mat_a.size)
print('data  = ', mat_a.data)

# COO形式
spmat_a_coo = scsp.coo_matrix(mat_a)
#print('COO A = \n', spmat_a_coo)
print('COO A :', spmat_a_coo.getformat())
print('dtype    = ', spmat_a_coo.dtype)
print('shape    = ', spmat_a_coo.shape)
print('ndim     = ', spmat_a_coo.ndim) # 常に2
print('nnz      = ', spmat_a_coo.nnz)
print('data[]   = ', spmat_a_coo.data)
print('row[]    = ', spmat_a_coo.row)
print('col[]    = ', spmat_a_coo.col)

# CSR形式
spmat_a_csr = scsp.csr_matrix(mat_a)
#print('CSR A = \n', spmat_a_csr)
print('CSR A : ', spmat_a_csr.getformat())
print('dtype    = ', spmat_a_csr.dtype)
print('shape    = ', spmat_a_csr.shape)
print('ndim     = ', spmat_a_csr.ndim) # 常に2
print('nnz      = ', spmat_a_csr.nnz)
print('data[]   = ', spmat_a_csr.data)
print('indices[]= ', spmat_a_csr.indices)
print('indptr[] = ', spmat_a_csr.indptr)

# CSC形式
spmat_a_csc = scsp.csc_matrix(mat_a)
#print('CSC A = \n', spmat_a_csc)
print('CSC A : ', spmat_a_csc.getformat())
print('dtype    = ', spmat_a_csc.dtype)
print('shape    = ', spmat_a_csc.shape)
print('ndim     = ', spmat_a_csc.ndim) # 常に2
print('nnz      = ', spmat_a_csc.nnz)
print('data[]   = ', spmat_a_csc.data)
print('indices[]= ', spmat_a_csc.indices)
print('indptr[] = ', spmat_a_csc.indptr)

# 密行列に戻す
print('CSR -> Dense: \n', spmat_a_csr.todense())
print('CSC -> Dense: \n', spmat_a_csc.todense())


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
