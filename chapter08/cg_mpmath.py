# cg_mpmath.py : 多倍長精度Conjugate-Gradient法
import numpy as np
import mpmath  # 多倍長精度計算
import mpmath.libmp  # 可能ならばgmpy2を使用
# 時間計測
import time

# 計算精度初期設定
mpmath.mp.dps = 30
input_dps = input('10進精度桁数 dps = ')
if int(input_dps) > mpmath.mp.dps:
    mpmath.mp.dps = int(input_dps)
print('10進精度桁数 = ', mpmath.mp.dps)


# CG法(mpmath版)
def cg(vec_x, mat_a, vec_b, rtol, atol, max_times):
    dim = vec_x.rows
    r = vec_b - mat_a * vec_x
    p = r
    init_norm_r = mpmath.norm(r)
    old_norm_r = init_norm_r
    # メインループ
    for times in range(max_times):
        ap = mat_a * p
        alpha = (r.T * p)[0] / (p.T * ap)[0]
        vec_x = vec_x + alpha * p
        r = r - alpha * ap
        new_norm_r = mpmath.norm(r)
        beta = new_norm_r * new_norm_r / (old_norm_r * old_norm_r)
        # 収束判定
        print(times, mpmath.nstr(new_norm_r / init_norm_r))
        if(new_norm_r <= (rtol * init_norm_r + atol)):
            break

        p = r + beta * p
        old_norm_r = new_norm_r

    return times, vec_x


# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# (1)
mat_a = mpmath.zeros(dim, dim)
for i in range(dim):
    for j in range(dim):
        mat_a[i, j] = mpmath.mpf(dim - max(i, j))

mat_a = mat_a.T * mat_a
# print(mat_a)

# x = [1 2 ... dim]
vec_true_x = mpmath.matrix([i for i in range(1, dim + 1)])
# nprint(vec_true_x)

# b = A * x
vec_b = mat_a * vec_true_x

# CG法実行
# vec_x := 0
vec_x = mpmath.zeros(dim, 1)
start_time1 = time.time()
iterative_times, vec_x = cg(vec_x, mat_a, vec_b, 1.0e-20, 0.0, dim * 10)
time1 = time.time() - start_time1

relerr = mpmath.norm(vec_x - vec_true_x) / mpmath.norm(vec_true_x)
print(
    'CG: iteration, time = ',
    iterative_times, time1,
    ', relerr(vec_x) = ', relerr
)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
