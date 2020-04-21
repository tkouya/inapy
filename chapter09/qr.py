# qr.py : QR分解法
import numpy as np
import scipy as spy
import scipy.linalg as slinalg
# 時間計測
import time

# QR分解法
def qr(mat_a, rtol, atol, max_times):
	row_dim, col_dim = mat_a.shape
	if row_dim != col_dim:
		return 0, 0
	
	dim = row_dim
	
	rq = mat_a
	old_diagonal = np.array([mat_a[i, i] for i in range(dim)])
	
	# メインループ
	for times in range(max_times):
		# QR分解
		q, r = slinalg.qr(rq, pivoting=False)
		# RQ生成
		rq = r @ q

		if times % 10 == 0:
			print('times = ', times)
			print(rq)

		new_diagonal = np.array([rq[i, i] for i in range(dim)])
		diff_diagonal = new_diagonal - old_diagonal
		
		# 収束判定
		if(np.linalg.norm(diff_diagonal) <= (rtol * np.linalg.norm(new_diagonal) + atol)):
			break
		
		old_diagonal = new_diagonal
		
	return rq, times

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# (1)
mat_a = np.zeros((dim, dim))
for i in range(dim):
    for j in range(dim):
        mat_a[i, j] = float(dim - max(i, j))

print('mat_a = ', mat_a)

# QR分解法実行
start_time1 = time.time()
qr, iterative_times = qr(mat_a, 1.0e-15, 0.0, 51)
time1  = time.time() - start_time1

print('QR: iteration, time = ', iterative_times, time1)
print(' i        eigenvalues ')
for i in range(dim):
	print(f'{i:2d} {qr[i, i]:25.17e}');
