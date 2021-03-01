# relerr_norm_complete.py: ベクトル，行列のノルム相対誤差
import numpy as np


# rE_p
def rE_p(approx_val, true_val, p):
    ret = np.linalg.norm(true_val - approx_val, p)

    norm_true_val = np.linalg.norm(true_val, p)
    if norm_true_val != 0:
        ret /= norm_true_val 

    return ret


# print relative_errors
def print_relative_errors(approx_val, true_val):
    # ノルム相対誤差
    print(f'rE1(approx_val)  = {rE_p(approx_val, true_val, 1):10.1e}')
    print(f'rE2(approx_val)  = {rE_p(approx_val, true_val, 2):10.1e}')
    print(f'rEi(approx_val)  = {rE_p(approx_val, true_val, np.inf):10.1e}')

    # 各成分の相対誤差の最小値と最大値
    tmp_fabs_true_val = np.array(np.fabs(true_val))
    tmp_fabs_true_val[tmp_fabs_true_val == 0.0] = 1.0
    print(f'min_relerr_approx_x  = {np.nanmin(np.fabs(true_val - approx_val) / tmp_fabs_true_val):10.1e}')
    print(f'max_relerr_approx_x  = {np.nanmax(np.fabs(true_val - approx_val) / tmp_fabs_true_val):10.1e}')


# 真のベクトル，真の行列
x = np.array([np.sqrt(2), np.exp(1), np.pi])
A = np.array([[np.exp(1), 1 / np.pi, 0], [np.sqrt(5), np.log10(2), 1 / 3], [-np.sqrt(2), 0, np.pi]])

print('x = ', x)
print('A = '); print(A)

# 近似ベクトル，近似行列
approx_x = np.array([1.4142, 2.7183, 3.1416])
approx_A = np.array([
    [ 2.7183, 0.31831, 0],
    [ 2.2361, 0.30103, 0.33333],
    [-1.4142, 0      , 3.1416]
])

print('approx_x = ', approx_x)
print('approx_A = '); print(approx_A)

# Ax
Ax = A.dot(x) # 真値
approx_Ax = approx_A.dot(approx_x) # 近似値
print('approx_Ax = ', approx_Ax)

# 相対誤差表示
print_relative_errors(approx_x, x)
print_relative_errors(approx_A, A)
print_relative_errors(approx_Ax, Ax)

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
