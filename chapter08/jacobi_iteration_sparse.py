# jacobi_iteration_sparse.py : Jacobi反復法(疎行列版)
import scipy.io as scio
import numpy as np
# 時間計測
import time


# Jacobi反復法
def jacobi_iteration_sparse(vec_x, mat_a_sp, diagonal_mat_a, vec_b, rtol, atol, max_times):
    dim = vec_x.size
    old_x = vec_x

    # メインループ
    for times in range(max_times):
        new_x_diff = (vec_b - mat_a_sp.dot(old_x)) / diagonal_mat_a

        # 収束判定
        if np.linalg.norm(new_x_diff) <= (rtol * np.linalg.norm(old_x) + atol):
            break

        old_x += new_x_diff

    return times, old_x


# Matrix Market形式ファイルの読み込み
# mtx_filename = 'bcsstm22'  # n = 138
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

# 対角要素を取り出し
diagonal_mat_a = spmat_a.diagonal()

# Jacobi反復法実行
# x := 0
x = np.zeros(col_dim)
start_time1 = time.time()
iterative_times, x = jacobi_iteration_sparse(x, spmat_a, diagonal_mat_a, b, 1.0e-10, 0.0, col_dim * 10)
time1 = time.time() - start_time1

# 相対誤差
relerr_vec = np.fabs(true_x - x) / np.fabs(x)
relerr_norm = np.linalg.norm(true_x - x) / np.linalg.norm(x)  # 2-norm

# 最大・最小相対誤差のindex
max_i = np.argmax(relerr_vec)
min_i = np.argmin(relerr_vec)

print(f'x[{max_i:5d}] = {x[max_i]:25.17e}, max relerr = {np.max(relerr_vec):7.1e}')
print(f'x[{min_i:5d}] = {x[min_i]:25.17e}, min relerr = {np.min(relerr_vec):7.1e}')
print(f'norm2_relerr = {relerr_norm:7.1e}')
print('time = ', time1)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
