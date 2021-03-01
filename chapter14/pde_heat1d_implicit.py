# pde_heat1d_implicit.py ：熱方程式ソルバー(陰的解法)
import numpy as np
import scipy as sc
import scipy.sparse as scsp
import scipy.sparse.linalg as scsplinalg

# 境界条件 x in [a, b]
a, b = 0.0, 1.0

# t in [t0, t_end]
t0, t_end = 0.0, 1.0


# ut0(x) = u(0, x), uxa(t) = u(t, a), uxb(t) = u(t, b)
def ut0(x):
    return 1.0


def uxa(t):
    return 0.0


def uxb(t):
    return 0.0


# h = delta t = (t_end - t0) / div_t
# k = delta x = (b - a) / div_x
div_t = 100
div_x = 5
h_t = (t_end - t0) / div_t
h_x = (b - a) / div_x

# t_k, x_j
t = [t0 + h_t * k for k in range(1, div_t + 1)]
x = [a + h_x * j for j in range(1, div_x)]
print('t = ', t)
print('x = ', x)

# s = h_t / h_x^2
s = h_t / (h_x ** 2)
# 三重対角行列生成(**)
dim = div_x - 2
e_upper = [0.0] + [-s] * (dim - 1)
e_diag  = [2.0 * s + 1.0] * dim
e_lower = [-s] * (dim - 1) + [0.0]
e_element = np.array([e_upper, e_diag, e_lower])
print('element = ', e_element)
E = scsp.dia_matrix((e_element, [1, 0, -1]), shape=(dim, dim))

print('s = ', s)
print('E = \n', E.toarray())

# LU分解
E_csc = E.tocsc()  # SuperLUはCSC形式のみ
lu_E = scsplinalg.splu(E_csc)  # LU分解
# u_k
u_k = np.array([ut0(x[j]) for j in range(dim)])
print('u_k   = ', u_k)

# E u_{k+1} = u_k
for k in range(div_t):
    u_kp1 = lu_E.solve(u_k)
    u_k = u_kp1

# u(t_end, x)
print('u = ', uxa(t_end), u_kp1, uxb(t_end))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
