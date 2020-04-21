# sparse_matrix_plot.py : 疎行列パターン
import scipy.io as sio
import scipy.sparse.linalg as splin
import matplotlib.pyplot as plt

import numpy as np

# Matrix Market形式ファイルの読み込み
mtx_filename = 'lns_3937/lns_3937.mtx'
spmat_info = sio.mminfo(mtx_filename) 
print('spmat_info = ', spmat_info)

row_dim = spmat_info[0]
col_dim = spmat_info[1]

# COO形式
spmat_a_coo = sio.mmread(mtx_filename)
print('spmat_a = ', spmat_a_coo)

# COO -> Dense(密)
mat_a = spmat_a_coo.toarray()

# プロット
plt.spy(mat_a, precision = 0.1, markersize = 1)
#plt.show()
plt.savefig('sparse_matrix.png')

