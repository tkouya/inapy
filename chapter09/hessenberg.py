# hessenberg.py: ハウスホルダー変換
import numpy as np
import scipy as spy
import scipy.linalg as sclinalg
# 時間計測
import time

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# (1)
mat_a = np.zeros((dim, dim))
for i in range(dim):
    for j in range(dim):
        mat_a[i, j] = float(dim - max(i, j))

print('mat_a = \n', mat_a)

# ハウスホルダー変換実行
start_time1 = time.time()
h, p = sclinalg.hessenberg(mat_a, calc_q=True)
time1 = time.time() - start_time1

print('time = ', time1)
print('H = \n', h)
print('P = \n', p)
print('P H P^* = \n', p @ h @ p.T.conj())


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
