# bicgstab_sample.py : 前処理付きBiCGSTAB法
import scipy.io as sio
import scipy.sparse.linalg as splin
import scipy.sparse as sp
import numpy as np

# Matrix Market形式ファイルの読み込み
# ftp://math.nist.gov/pub/MatrixMarket2/Harwell-Boeing/oilgen/orsreg_1.mtx.gz
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

# 前処理用LinearOperatorセッティング
spmat_a_csc = spmat_a_coo.tocsc() # SuperLUはCSC形式のみ
spmat_ilu = splin.spilu(spmat_a_csc) # ILU分解
# matvecはM^(-1) * vec処理
spmat_m = splin.LinearOperator(spmat_ilu.shape, matvec=spmat_ilu.solve)

# 前処理付きBiCGSTAB
x,info = splin.bicgstab(spmat_a, b, M=spmat_m)
# 前処理なし
#x,info = splin.bicgstab(spmat_a, b)

# 解表示
print('x = ', x)
print('info = ', info)

# 相対誤差
relerr_vec = np.fabs(true_x - x) / np.fabs(x)
print('max relerr = ', np.max(relerr_vec))
print('min relerr = ', np.min(relerr_vec))
