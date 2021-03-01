# sparse_matrix_lu.py : 疎行列の取り扱いと直接法
import scipy.io as scio
import scipy.sparse.linalg as scsplinalg
import numpy as np

# Matrix Market形式ファイルの読み込み
# mtx_filename = 'bcsstm22'  # n = 138
# mtx_filename = 'orani678'  # n = 2529
# mtx_filename = 'lns_3937'  # n = 3937
mtx_filename = 'memplus'   # n = 17758

mtx_filename_full = mtx_filename + '.mtx'
spmat_info = scio.mminfo(mtx_filename_full)
print('spmat_info = ', spmat_info)

row_dim = spmat_info[0]
col_dim = spmat_info[1]

# COO形式
spmat_a_coo = scio.mmread(mtx_filename_full)
print('spmat_a = ', spmat_a_coo)

# COO -> CSR
spmat_a = spmat_a_coo.tocsr()

# x = [1, 2, ..., n]
true_x = np.array(np.arange(1, col_dim + 1))
print('true_x = ', true_x)
b = spmat_a.dot(true_x)
print('b = ', b)

# 連立一次方程式を解く(1)
# x = scsplinalg.spsolve(spmat_a, b)

# 連立一次方程式を解く(2) LU分解+前進・後退代入
spmat_a_csc = spmat_a_coo.tocsc()  # cscであることを求められる
spmat_lu = scsplinalg.splu(spmat_a_csc)  # LU分解
x = spmat_lu.solve(b)  # 前進・後退代入

print('x = ', x)

# 相対誤差
relerr_vec = np.fabs(true_x - x) / np.fabs(x)
relerr_norm = np.linalg.norm(true_x - x) / np.linalg.norm(x)  # 2-norm

# 最大・最小相対誤差のindex
max_i = np.argmax(relerr_vec)
min_i = np.argmin(relerr_vec)

print(f'x[{max_i:5d}] = {x[max_i]:25.17e}, max relerr = {np.max(relerr_vec):7.1e}')
print(f'x[{min_i:5d}] = {x[min_i]:25.17e}, min relerr = {np.min(relerr_vec):7.1e}')
print(f'norm2_relerr = {relerr_norm:7.1e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
