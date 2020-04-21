# sparse_matrix.py : 疎行列の取り扱い
import scipy.io as sio
import scipy.sparse.linalg as splin
import scipy.sparse as sp
import numpy as np

# Matrix Market形式ファイルの読み込み
#mtx_filename = 'lns_3937/lns_3937.mtx'
mtx_filename = 'orsreg_1.mtx'
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

# 連立一次方程式を解く
#x = splin.spsolve(spmat_a, b); info = 0

# 前処理
spmat_a_csc = spmat_a_coo.tocsc() # SuperLUはCSC形式のみ
spmat_ilu = splin.spilu(spmat_a_csc) # ILU分解
# matvecはM^(-1) * vec処理
spmat_m =  splin.LinearOperator(spmat_ilu.shape, matvec=spmat_ilu.solve)
x,info = splin.bicgstab(spmat_a, b, M=spmat_m) # 前処理付きBiCGSTAB
#x,info = splin.bicgstab(spmat_a, b)
#x,info = splin.lgmres(spmat_a, b, M=spmat_m)

#x,info = splin.bicg(spmat_a, b)
#x,info = splin.bicgstab(spmat_a, b)
#x,info = splin.gmres(spmat_a, b)
#x,info = splin.lgmres(spmat_a, b)
print('x = ', x)
print('info = ', info)

# 相対誤差
relerr_vec = np.fabs(true_x - x) / np.fabs(x)
print('max relerr = ', np.max(relerr_vec))
print('min relerr = ', np.min(relerr_vec))
