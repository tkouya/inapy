# pde_heat1d.py ：熱方程式ソルバー
import numpy as np # NumPy
import scipy as sp # SciPy
import scipy.sparse as spsp # Sparse
import scipy.sparse.linalg as spsplin # Sparse Linear Algebra

# 境界条件 x in [a, b]
a, b = 0.0, 1.0

# t in [t0, t_end]
t0, t_end = 0.0, 1.0

# ut0(x) = u(0, x), uxa(t) = u(t, a), uxb(t) = u(t, b)
ut0 = lambda x: 1.0
uxa = lambda t: 0.0
uxb = lambda t: 0.0

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

# 三重対角行列生成
dim = div_x - 2
d_upper = [0.0] + [1.0] * (dim - 1)
d_diag  = [-2.0] * dim
d_lower = [1.0] * (dim - 1) + [0.0]
d_element = np.array([d_upper, d_diag, d_lower])
#print('element = ', c_element)
D = spsp.dia_matrix((d_element, [1, 0, -1]), shape=(dim, dim))
IpsD = spsp.eye(dim) + s * D

print('s = ', s)
print('I + sD = '); print(IpsD.toarray())

# u_k
u_k = np.array([ut0(x[j]) for j in range(dim)])
print('u_k   = ', u_k)

# u_{k+1} := (I + sD) u_k
for k in range(div_t):
    u_kp1 = IpsD @ u_k
    u_k = u_kp1
    t = t0 + (k + 1) * h_t
    print(f'{t:10.3e}, {uxa(t):15.7e}') {u_kp1:15.7e}, {uxb(t):15.7e}')

# u(t_end, x)
print('u = ', uxa(t_end), u_kp1, uxb(t_end))
