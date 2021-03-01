# pde_wave1d.py: 波動方程式ソルバー
import numpy as np
import scipy.sparse as scsp

# 境界条件 x in [a, b]
a, b = 0.0, 1.0

# t in [t0, t_end]
t0, t_end = 0.0, 10.0


# alpha(t) = u(t, a), beta(t) = u(t, b)
def alpha(t):
    return np.exp(-t / 2.0)


def beta(t):
    return 1.0


# u0(x) = u(0, x), v0(t) = Du(0, x)
def u0(x):
    return 0.0


def v0(x):
    return 0.0


# h = delta t = (t_end - t0) / div_t
# k = delta x = (b - a) / div_x
div_t = 1000
div_x = 50
h_t = (t_end - t0) / div_t
h_x = (b - a) / div_x

# t_k, x_j
t = [t0 + h_t * k for k in range(1, div_t + 1)]
x = [a + h_x * j for j in range(1, div_x)]
print('t = ', t)
print('x = ', x)

# lambda = h_x / h_t
nlambda = h_x / h_t
print('lambda = ', nlambda)
if nlambda > 1:
    print('!!! Not Converge !!!!')

# r2 = (c * h / k)^2
c = 1.0
r2 = (c * h_t / h_x) ** 2

# 三重対角行列生成
dim = div_x - 2
c_upper = [0.0] + [r2] * (dim - 1)
c_diag = [2.0 * (1 - r2)] * dim
c_lower = [r2] * (dim - 1) + [0.0]
c_element = np.array([c_upper, c_diag, c_lower])
print('element = \n', c_element)
C = scsp.dia_matrix((c_element, [1, 0, -1]), shape=(dim, dim))

print('C = \n', C.toarray())

# u_{k-1}, u_k
u_km1 = np.array([u0(x[j]) - 2 * h_t * v0(x[j]) for j in range(dim)])
u_k = np.array([u0(x[j]) for j in range(dim)])
print('u_km1 = ', u_km1)
print('u_k   = ', u_k)

# u_{k+1} := C u_k - u_{k-1} + r2 [u_k0 0...0 u_km]
for k in range(div_t):
    u_kp1 = C @ u_k - u_km1
    u_kp1[0] += r2 * alpha(t[k])
    u_kp1[dim - 1] += r2 * beta(t[k])

    u_km1 = u_k
    u_k = u_kp1

# u(t_end, x)
print('u = ', alpha(t_end), u_kp1, beta(t_end))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
