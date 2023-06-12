# power_eig.py: べき乗法
import numpy as np
import scipy as sc
import scipy.linalg as sclinalg


# べき乗法
def power_eig(init_max_ev, mat_a, max_times, rtol=1.0e-10, atol=1.0e-50):
    old_ev = init_max_ev
    tmp_ev = old_ev

    # 絶対値最大成分を取得
    index = np.abs(old_ev).argmax()
    old_max_eig = old_ev[index]
    old_ev /= old_max_eig

    # メインループ
    for times in range(max_times):
        tmp_ev = mat_a.dot(old_ev)
        new_max_eig = tmp_ev[index]

        if np.abs(new_max_eig - old_max_eig) <= np.abs(old_max_eig) * rtol + atol:
            break

        index = np.abs(tmp_ev).argmax()
        old_max_eig = new_max_eig
        new_max_eig = tmp_ev[index]
        old_ev = tmp_ev / new_max_eig
        print(f'{times:5d}, {new_max_eig:25.17e}')

    max_ev = tmp_ev / np.linalg.norm(tmp_ev)

    return times, new_max_eig, max_ev


# 逆べき乗法
def inv_power_eig(init_max_ev, mat_a, max_times, rtol=1.0e-10, atol=1.0e-50):
    old_ev = init_max_ev
    tmp_ev = old_ev

    # 絶対値最大成分を取得
    index = np.abs(old_ev).argmax()
    old_max_eig = old_ev[index]
    old_ev /= old_max_eig

    # LU分解
    mat_lu, pivot = sclinalg.lu_factor(mat_a)

    # メインループ
    for times in range(max_times):
        tmp_ev = sclinalg.lu_solve((mat_lu, pivot), old_ev)
        new_max_eig = tmp_ev[index]

        if np.abs(new_max_eig - old_max_eig) <= np.abs(old_max_eig) * rtol + atol:
            break

        index = np.abs(tmp_ev).argmax()
        old_max_eig = new_max_eig
        new_max_eig = tmp_ev[index]
        old_ev = tmp_ev / new_max_eig
        print(f'{times:5d}, {1.0 / new_max_eig:25.17e}')

    max_ev = tmp_ev / np.linalg.norm(tmp_ev)

    return times, 1.0 / new_max_eig, max_ev


# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# 乱数行列をAとして与える
np.random.seed(20190515)
mat_a = sc.random.rand(dim, dim)
# 対称行列化
for i in range(dim):
    for j in range(i):
        mat_a[i, j] = mat_a[j, i]

# 行列確認
print('A = ', mat_a)

# 固有値と固有ベクトル
eigval, ev = sclinalg.eig(mat_a)
ev = ev.T
print('Eigenvalues = ', eigval)
print('Eigenvectors = ', ev)

# A * v = lambda * v ?
for i in range(0, eigval.size):
    print('|| A * v - lambda[', i, '] * v||_2 = ', sclinalg.norm(mat_a @ ev[i].T - eigval[i] * ev[i]))

# べき乗法実行
max_ev = sc.random.rand(dim)
itimes, max_eig, max_ev = power_eig(max_ev, mat_a, dim, 1.0e-13)
print('iterative times = ', itimes)
print('max_eig = ', max_eig)
print('max_ev = ', max_ev)

# 逆べき乗法実行
min_ev = sc.random.rand(dim)
itimes, min_eig, min_ev = inv_power_eig(min_ev, mat_a, dim, 1.0e-13)
print('iterative times = ', itimes)
print('min_eig = ', min_eig)
print('min_ev = ', min_ev)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
