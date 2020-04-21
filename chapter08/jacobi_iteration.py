# jacobi_iteration.py : Jacobi反復法, Gauss-Seidel法，SOR法
import numpy as np
import scipy as spy
import scipy.linalg as slinalg
# 時間計測
import time

# Jacobi反復法
def jacobi_iteration(vec_x, mat_a, vec_b, rtol, atol, max_times):
	dim = vec_x.size
	old_x = vec_x

	# 対角成分取得
	diagonal_mat_a = np.array([mat_a[i, i] for i in range(dim)])

	# メインループ
	for times in range(max_times):
		new_x_diff = (vec_b - mat_a @ old_x) / diagonal_mat_a

		# 収束判定
		if(np.linalg.norm(new_x_diff) <= (rtol * np.linalg.norm(old_x) + atol)):
			old_x += new_x_diff
			break

		old_x += new_x_diff

	return times, old_x

# Gauss-Seidel法
def gauss_seidel(vec_x, mat_a, vec_b, rtol, atol, max_times):
	dim = vec_x.size
	old_x = vec_x
	new_x = old_x
	new_x_diff = np.zeros(dim)

	# 対角成分取得
	print(dim)
	diagonal_mat_a = np.array([mat_a[i, i] for i in range(dim)])

	# メインループ
	for times in range(max_times):

		# old_xとnew_xを使用する行列ベクトル積
		for i in range(dim):

			# new_x_sum
			new_x_sum = 0.0
			for j in range(i):
				new_x_sum += mat_a[i, j] * new_x[j]

			# old_x_sum
			old_x_sum = 0.0
			for j in range(i, dim):
				old_x_sum += mat_a[i, j] * old_x[j]

			new_x_diff[i] = (vec_b[i] - new_x_sum - old_x_sum) / diagonal_mat_a[i]
			new_x[i] = old_x[i] + new_x_diff[i]

		# 収束判定
		if(np.linalg.norm(new_x_diff) <= (rtol * np.linalg.norm(old_x) + atol)):
			break

		old_x = new_x

	return times, new_x

# SOR法
def sor(vec_x, mat_a, vec_b, rtol, atol, max_times, omega):
	dim = vec_x.size
	old_x = vec_x
	new_x = old_x
	new_x_diff = np.zeros(dim)

	# 対角成分取得
	print(dim)
	diagonal_mat_a = np.array([mat_a[i, i] for i in range(dim)])

	# メインループ
	for times in range(max_times):

		# old_xとnew_xを使用する行列ベクトル積
		for i in range(dim):

			# new_x_sum
			new_x_sum = 0.0
			for j in range(i):
				new_x_sum += mat_a[i, j] * new_x[j]

			# old_x_sum
			old_x_sum = 0.0
			for j in range(i, dim):
				old_x_sum += mat_a[i, j] * old_x[j]

			new_x_diff[i] = omega / diagonal_mat_a[i] * (vec_b[i] - new_x_sum - old_x_sum)
			new_x[i] = old_x[i] + new_x_diff[i]

		# 収束判定
		if(np.linalg.norm(new_x_diff) <= (rtol * np.linalg.norm(old_x) + atol)):
			break

		old_x = new_x

	return times, new_x

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

# x = [1 2 ... dim]
vec_true_x = spy.arange(1, dim + 1)
#print(vec_true_x)

# b = A * x
vec_b = mat_a @ vec_true_x


# Jacobi反復法実行
# vec_x := 0
vec_x = np.zeros(dim)
start_time1 = time.time()
iterative_times, vec_x = jacobi_iteration(vec_x, mat_a, vec_b, 1.0e-10, 0.0, dim * 10)
time1  = time.time() - start_time1

relerr = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('Jacobi: iteration, time = ', iterative_times, time1, ', relerr(vec_x) = ', relerr)

# Gauss-Seidel法実行
# vec_x := 0
vec_x = np.zeros(dim)

start_time2 = time.time()
iterative_times, vec_x = gauss_seidel(vec_x, mat_a, vec_b, 1.0e-10, 0.0, dim * 10)
time2  = time.time() - start_time2

relerr = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('GS: iteration, time = ', iterative_times, time2, ', relerr(vec_x) = ', relerr)


# SOR法実行
sor_omega = 1.5
# vec_x := 0
vec_x = np.zeros(dim)

start_time3 = time.time()
iterative_times, vec_x = sor(vec_x, mat_a, vec_b, 1.0e-10, 0.0, dim * 10, sor_omega)
time3  = time.time() - start_time3

relerr = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('SOR(', sor_omega, ') iteration, time = ', iterative_times, time3, ', relerr(vec_x) = ', relerr)


