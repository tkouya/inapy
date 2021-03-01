# pde_poisson.py ：ポワソン方程式ソルバー
import numpy as np
import scipy.sparse as scsp
import scipy.sparse.linalg as scsplinalg


# ポワソン方程式用の係数行列生成
def poisson_2d_matrix(h, n, ldim):

    # 対角ブロック成分
    tmp_diag_element = np.array([
        [ 1.0] * (n - 1),
        [-4.0] * (n - 1),
        [ 1.0] * (n - 1)
    ])
    poisson_diag_mat = scsp.spdiags(tmp_diag_element, [-1, 0, 1], n - 1, n - 1)

    # ポワソン方程式の係数行列生成
    # I kprod A + L kprod B
    # L: Tridiagonal matrix with all one element - I
    poisson_mat_pattern = scsp.spdiags(
        np.array([[1] * ldim, [0] * ldim, [1] * ldim]),
        [-1, 0, 1],
        ldim,
        ldim
    )
    poisson_mat = scsp.kron(scsp.eye(ldim), poisson_diag_mat) + scsp.kron(poisson_mat_pattern, scsp.eye(n - 1))
    print(poisson_mat.toarray())

    return poisson_mat


# g(x, y)
def gfunc(x, y):
    return -1.0


# 定数ベクトルb生成
def poisson_2d_vec(min_x, max_x, num_div_x, min_y, max_y, num_div_y):
    b = np.array([0.0] * ((num_div_x - 1) * (num_div_y - 1)))
    h_x = (max_x - min_x) / num_div_x
    h_y = (max_y - min_y) / num_div_y
    for i in range(1, num_div_x):
        x = min_x + h_x * i
        index = (num_div_x - 1) * (i - 1)
        for j in range(1, num_div_y):
            y = min_y + h_y * j
            b[index] = gfunc(x, y)
            index += 1

    return b


# ブロック疎行列生成
n = 8  # x, y方向分割数
num_div_x = n
num_div_y = n

# x in [min_x, max_x]
min_x, max_x = 0.0, 1.0

# y in [min_y, max_y]
min_y, max_y = min_x, max_x

# x, y座標値をセット
x = np.linspace(min_x, max_x, num_div_x)
y = np.linspace(min_y, max_y, num_div_y)

h = (max_x - min_x) / float(n) ** 2
ldim = n - 1  # ブロック数

# 行列生成
spmat = poisson_2d_matrix(h, n, ldim)
print(spmat)
# to CSR
spmat_a = scsp.csr_matrix(spmat)

# 定数ベクトル生成
vec_b = poisson_2d_vec(min_x, max_x, num_div_x, min_y, max_y, num_div_y)
vec_b = h * vec_b
print(vec_b)

# 連立一次方程式を解く
tmp_u = scsplinalg.spsolve(spmat_a, vec_b)
print('tmp_u = ', tmp_u)

# u(x, y)を表示
u = np.array([[0.0] * (num_div_x + 1)] * (num_div_y + 1))
for i in range(1, num_div_x):
    for j in range(1, num_div_y):
        u[i, j] = tmp_u[(i - 1) * (num_div_x - 1) + (j - 1)]

print(u)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
