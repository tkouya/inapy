# pde_poisson.py ：Poisson方程式ソルバー
import numpy as np
import scipy as spy
import scipy.sparse as spysp
import scipy.sparse.linalg as spylin

# Poisson方程式用の係数行列生成
def poisson_2d_matrix(h, n, l):

    # 対角ブロック成分
    tmp_diag_element = np.array([
        [ 1.0] * (n - 1),
        [-4.0] * (n - 1),
        [ 1.0] * (n - 1)
    ])
    poisson_diag_mat = spysp.spdiags(tmp_diag_element, [-1, 0, 1], n - 1, n - 1)

    # Poisson方程式の係数行列生成
    # I kprod A + L kprod B
    # L: Tridiagonal matrix with all one element - I
    poisson_mat_pattern = spysp.spdiags(np.array([[1] * l, [0] * l, [1] * l]), [-1, 0, 1], l, l)
    poisson_mat = spysp.kron(spysp.eye(l), poisson_diag_mat) + spysp.kron(poisson_mat_pattern, spysp.eye(n - 1))
    print(poisson_mat.toarray())

    return poisson_mat

# g(x, y)
def gfunc(x, y):
    return 1.0

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
n = 8 # x, y方向分割数
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
l = n - 1 #ブロック数

# 行列生成
spmat = poisson_2d_matrix(h, n, l)
#print(spmat)
# to CSR
spmat_a = spysp.csr_matrix(spmat)

# 定数ベクトル生成
vec_b = poisson_2d_vec(min_x, max_x, num_div_x, min_y, max_y, num_div_y)
vec_b = h * vec_b
print(vec_b)

# 連立一次方程式を解く
# 前処理用LinearOperatorセッティング
spmat_a_csc = spmat_a.tocsc() # SuperLUはCSC形式のみ
spmat_ilu = spylin.spilu(spmat_a_csc) # ILU分解
# matvecはM^(-1) * vec処理
spmat_m = spylin.LinearOperator(spmat_ilu.shape, matvec=spmat_ilu.solve)

# 前処理付きCG
tmp_u,info = spylin.cg(spmat_a, vec_b, M=spmat_m)

# 前処理なし
#tmp_u = spylin.spsolve(spmat_a, vec_b); info = 0
#x,info = splin.bicg(spmat_a, b)
#x,info = splin.bicgstab(spmat_a, b)
#x,info = splin.gmres(spmat_a, b)
#x,info = splin.lgmres(spmat_a, b)
print('tmp_u = ', tmp_u)
print('info = ', info)

# u(x, y)を表示
u = np.array([[0.0] * (num_div_x + 1)] * (num_div_y + 1))
for i in range(1, num_div_x):
    for j in range(1, num_div_y):
        u[i, j] = tmp_u[(i - 1) * (num_div_x - 1) + (j - 1)]

print(u)