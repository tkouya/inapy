# 数値微分
import scipy.misc as smisc
import numpy as np

# 中央差分式の係数(奇数点数のみ)を出力
for m in range(1, 6):
	print('--- ', m, '階差分 ---')
	if m >= 3:
		min_num_points = 2 * m - 1
	else:
		min_num_points = 3
	for n in range(min_num_points, 10, 2):
		print(n, '点公式: ', smisc.central_diff_weights(n, m))

# 相対誤差
def relerr(approx, true_val):
	relerr_val = np.abs(approx - true_val)
	if true_val != 0: relerr_val /= np.abs(true_val)

	return relerr_val

# 中央差分式に基づく数値微分

# 元の関数
def org_func(x):
#	return np.sin(np.cos(x))
	return np.exp(np.sin(x))

# 1階導関数
def diff_func(x):
#	return np.cos(np.cos(x)) * (-np.sin(x))
	return np.exp(np.sin(x)) * np.cos(x)

# 数値微分
x = 1.5
print('真値                 = ', diff_func(x))

approx_diff = smisc.derivative(org_func, x)
print(f'中央差分商   標準設定: {approx_diff:25.17e} {relerr(approx_diff, diff_func(x)):10.3e}')

n = 3
dx = 0.1
approx_diff = smisc.derivative(org_func, x, dx, order = n)
print(f'中央差分商 {n:3d}点公式 : {approx_diff:25.17e} {relerr(approx_diff, diff_func(x)):10.3e}')

n = 5
dx = 0.1
approx_diff = smisc.derivative(org_func, x, dx, order = n)
print(f'中央差分商 {n:3d}点公式 : {approx_diff:25.17e} {relerr(approx_diff, diff_func(x)):10.3e}')

# 最高精度を求める
min_approx = 0.0
min_relerr = 1.0
min_n = 3
min_dx = 0.1

print('dx -> ', end = '')
for dx in np.logspace(1, 10, num=10, endpoint=1.0e-15, base = 0.1):
	print(f'{dx:10.3e}', end = ' ')
print()
for n in range(3, 20, 2):
	print(f'{n:3d}', end = ':')
	for dx in np.logspace(1, 10, num=10, endpoint=1.0e-15, base = 0.1):
		approx_diff = smisc.derivative(org_func, x, dx, order = n)
		relerr_val = relerr(approx_diff, diff_func(x))
		print(f'{relerr_val:10.3e}', end = ' ')
		if min_relerr > relerr_val :
			min_approx = approx_diff
			min_relerr = relerr_val
			min_n = n
			min_dx = dx
	print()

print('最高精度:')
print(f'n = {min_n:3d}, dx = {min_dx:10.3e}, relerr = {min_relerr:10.3e}, approx_diff = {min_approx:25.17e}')
