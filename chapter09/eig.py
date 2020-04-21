# eig.py: 行列の固有値と固有ベクトル
import numpy as np
import scipy as spy
import scipy.linalg as slinalg

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# 乱数行列をAとして与える
np.random.seed(20190515)
mat_a = spy.random.rand(dim, dim)

# 行列確認
print('A = ', mat_a)

# 固有値と固有ベクトル
eigval, ev = slinalg.eig(mat_a)
ev = ev.T
print('Eigenvalues = ', eigval)
print('Eigenvectors = ', ev)

# A * v = lambda * v ?
for i in range(0, eigval.size) :
	print('|| A * v - lambda[', i, '] * v||_2 = ', slinalg.norm(mat_a @ ev[i].T - eigval[i] * ev[i]))

