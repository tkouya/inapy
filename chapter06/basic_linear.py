# basic_linear.py: 基本線型計算
import numpy as np
import scipy.linalg as sclinalg

# ベクトル
vec_a = np.array([1, 2, 3])
vec_b = np.array([-3, -2, -1])

print('vec_a = ', vec_a)
print('vec_b = ', vec_b)

# BLAS Level1
# ベクトル演算

# スカラー倍，加減算
# c := 3 * a + b, d ;= 2^(1/2) * a - 3^(1/3) * b

# 内積
ip_ab = vec_a.dot(vec_b)
print('(a, b) = ', ip_ab)

vec_c = np.array([1 + 1j, -2 + 2j])
vec_d = np.array([-2 + 3j, -1 - 4j])
print('vec_c = ', vec_c)
print('vec_d = ', vec_d)

dot_cd = vec_c.dot(vec_d)
ip_cd = np.conj(vec_c).dot(vec_d)
print(' c . d = ', dot_cd)
print('(c, d) = ', ip_cd)

# ユークリッドノルム
print('||vec_a||_2 = ', np.linalg.norm(vec_a))
print('||vec_a||_2 = ', sclinalg.norm(vec_a))

# 1ノルム
print('||vec_a||_1 = ', np.linalg.norm(vec_a, 1))
print('||vec_a||_1 = ', sclinalg.norm(vec_a, 1))

# 無限大ノルム
print('||vec_a||_inf = ', np.linalg.norm(vec_a, np.inf))
print('||vec_a||_inf = ', sclinalg.norm(vec_a, np.inf))

# 複素ベクトル, j = sqrt(-1)
vec_ai = np.array([1j, 2j, 3j])
vec_bi = np.array([-3 - 1j, -2 - 5j, -1 + 1j])

print('vec_ai = ', vec_ai)
print('vec_bi = ', vec_bi)

vec_ci = vec_ai + vec_bi
vec_di = 2**(1/2) * vec_ai - 3**(1/3) * vec_bi

print('vec_ci = ', vec_ci)
print('vec_di = ', vec_di)

ip_aibi = vec_ai.dot(vec_bi)
print('(ai, bi) = ', ip_aibi)

# BLAS Level2
# 行列，ベクトル演算

# 行列
mat_a = np.array([[1, 2, 3], [2, 2, 3], [3, 3, 3]])
print('mat_a = \n', mat_a)

# 行列・ベクトル積
mat_av = mat_a.dot(vec_a)
print('A * a = ', mat_av)

# BLAS Level3
# 行列演算
mat_b = np.array([[-3, -3, -3], [-3, -2, -2], [-3, -2, -1]])
mat_ab = mat_a.dot(mat_b)
print('A * B = \n', mat_ab)
mat_ab_at = mat_a @ mat_b
print('A @ B = \n', mat_ab_at)

# 単位行列
I3 = np.eye(3)
print('I = \n', I3)

# 逆行列
inv_mat_a = np.linalg.inv(mat_a)
print('A^(-1) = \n', inv_mat_a)

# || A * A^(-1) - I ||_2
ret = mat_a @ inv_mat_a
print(' A * A^(-1) = \n', ret)
ret = ret - I3
print(' A * A^(-1) - I3 = \n', ret)
print('|| A^(-1) * A - I ||_2 = ', '{:25.17e}'.format(np.linalg.norm(ret)))
print('|| A^(-1) * A - I ||_2 = ', '{:25.17e}'.format(sclinalg.norm(ret)))
print('|| A^(-1) * A - I ||_F = ', '{:25.17e}'.format(np.linalg.norm(ret, 'fro')))
print('|| A^(-1) * A - I ||_F = ', '{:25.17e}'.format(sclinalg.norm(ret, 'fro')))
print('|| A^(-1) * A - I ||_1 = ', '{:25.17e}'.format(np.linalg.norm(ret, 1)))
print('|| A^(-1) * A - I ||_1 = ', '{:25.17e}'.format(sclinalg.norm(ret, 1)))
print('|| A^(-1) * A - I ||_1 = ', '{:25.17e}'.format(np.linalg.norm(ret, np.inf)))
print('|| A^(-1) * A - I ||_inf = ', '{:25.17e}'.format(sclinalg.norm(ret, np.inf)))

# rank(A) : numpyのみ
rank_a = np.linalg.matrix_rank(mat_a)
print('rank(A) = ', '{:25.17e}'.format(rank_a))

# cond(A) : numpyのみ
h_mat = sclinalg.hilbert(3)
inv_h_mat = sclinalg.invhilbert(3)
print('Hilbert matrix = \n', h_mat)
print('Inverse Hilbert matrix = \n', inv_h_mat)
print('||H * H^(-1) - I3 = \n', sclinalg.norm(h_mat @ inv_h_mat - I3))
print('cond(H) = ', np.linalg.cond(h_mat))
print('||H||_2 * ||H^(-1)||_2 = ', np.linalg.norm(h_mat) * np.linalg.norm(inv_h_mat))
print('cond(H, 1) = ', np.linalg.cond(h_mat, 1))
print('||H||_1 * ||H^(-1)||_1 = ', np.linalg.norm(h_mat, 1) * np.linalg.norm(inv_h_mat, 1))
print('cond(H, np.inf) = ', np.linalg.cond(h_mat, 1))
print('||H||_inf * ||H^(-1)||_inf = ', np.linalg.norm(h_mat, np.inf) * np.linalg.norm(inv_h_mat, np.inf))

# det(A)
p_mat = sclinalg.pascal(3)
print('Pascal matrix = \n', p_mat)
print('det(P) = |P| = ', sclinalg.det(p_mat))

# Companion行列と固有値
# p(x) = x^3 + x^2 + x + 1 = 0
poly_coef = [1, 1, 1, 1]
mat_c = sclinalg.companion(poly_coef)
print('Companion matrix = \n', mat_c)
eigval, ev = sclinalg.eig(mat_c)
ev = ev.T
print('Eigenvalues = ', eigval)
print('Eigenvectors = ', ev)
# C * v = lambda * v ?
for i in range(0, eigval.size):
    print('|| C * v - lambda[', i, '] * v||_2 = ', sclinalg.norm(mat_c @ ev[i].T - eigval[i] * ev[i]))

# p(lambda) = 0?
eigpoly = np.poly1d(poly_coef)
for i in range(eigval.size):
    print('p(lambda[', i, ']) = ', eigpoly(eigval[i]))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
