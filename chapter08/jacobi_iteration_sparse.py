# jacobi_iteration_sparse.py : Jacobi反復法(疎行列版)
import numpy as np
import scipy as spy
import scipy.linalg as slinalg
import scipy.sparse as spysp
# 時間計測
import time

# Jacobi反復法
def jacobi_iteration_sparse(vec_x, mat_a_sp, diagonal_mat_a, vec_b, rtol, atol, max_times):
	dim = vec_x.size
	old_x = vec_x

	# メインループ
	for times in range(max_times):
		new_x_diff = (vec_b - mat_a_sp.dot(old_x)) / diagonal_mat_a

		# 収束判定
		if(np.linalg.norm(new_x_diff) <= (rtol * np.linalg.norm(old_x) + atol)):
			break

		old_x += new_x_diff

	return times, old_x


# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# 三重対角行列
mat_a = np.zeros((dim, dim))
for i in range(1, dim):
	mat_a[i, i - 1] = -1.0
for i in range(dim):
	mat_a[i, i] = 2.0
for i in range(dim - 1):
	mat_a[i, i + 1] = -1.0

print(mat_a)

# 対角成分設定
diagonal_mat_a = np.array([mat_a[i, i] for i in range(dim)])

# 行列Aを疎行列化
mat_a_sp = spysp.csr_matrix(mat_a)

# x = [1 2 ... dim]
vec_true_x = spy.arange(1, dim + 1)
#print(vec_true_x)

# b = A * x
vec_b = mat_a_sp.dot(vec_true_x)

# Jacobi反復法実行
# vec_x := 0
vec_x = np.zeros(dim)
start_time1 = time.time()
iterative_times, vec_x = jacobi_iteration_sparse(vec_x, mat_a_sp, diagonal_mat_a, vec_b, 1.0e-10, 0.0, dim * 10)
time1  = time.time() - start_time1

relerr = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('Jacobi: iteration, time = ', iterative_times, time1, ', relerr(vec_x) = ', relerr)
