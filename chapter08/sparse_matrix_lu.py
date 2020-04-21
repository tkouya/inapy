# sparse_matrix.py : 疎行列の取り扱い
import scipy.io as sio
import scipy.sparse as sp
import scipy.sparse.linalg as splin
import numpy as np

# Matrix Market形式ファイルの読み込み
#mtx_filename = 'lns_3937/lns_3937.mtx'
mtx_filename = 'lnsp3937.mtx'
spmat_info = sio.mminfo(mtx_filename) 
print('spmat_info = ', spmat_info)

row_dim = spmat_info[0]
col_dim = spmat_info[1]

# COO形式
spmat_a_coo = sio.mmread(mtx_filename)
print('spmat_a = ', spmat_a_coo)

# COO -> CSR
spmat_a = spmat_a_coo.tocsr()

# x = [1, 2, ..., n]
true_x = np.array(np.arange(1, col_dim + 1))
print(true_x)
b = spmat_a.dot(true_x)
print(b)

# 連立一次方程式を解く(1)
x = splin.spsolve(spmat_a, b)
# LU分解
#spmat_a_csc = spmat_a_coo.tocsc() # cscであることを求められる
#x = spmat_a_csc.dot(true_x)
#spmat_lu = splin.splu(spmat_a_csc)
#spmat_lu.solve(x)
print('x = ', x)

# 相対誤差
relerr_vec = np.fabs(true_x - x) / np.fabs(x)
print('max relerr = ', np.max(relerr_vec))
print('min relerr = ', np.min(relerr_vec))
