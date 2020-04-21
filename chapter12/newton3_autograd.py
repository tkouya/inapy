# Newton法
# import numpy as np
import autograd.numpy as np
import autograd
import scipy.optimize as sopt

# f(x) = 0
def func(x):
	return np.array([x[0] + x[1] - 3, x[0] * x[1] - 2])

# f'(x) = 0
def dfunc(x):
	return np.array([
		[1, 1],
		[x[1], x[0]]
	])

# autograd.jacobian
def dfunc_ag(x):
	# autogradによるJacobi行列の計算
	jacobi_mat = autograd.jacobian(func)(x)
	return jacobi_mat

x0 = np.array([10, -10], dtype = float) # 強制的にfloat型にすること！

# root関数(1)
final = sopt.root(func, x0)

# 表示
print('最終 -> x =')
for i in range(0, (final.x).size):
	print(f'{i:3d}, {final.x[i]:25.17e}')

print('検算 -> f(x) = ')
for i in range(0, (final.fun).size):
	print(f'{i:3d}, {final.fun[i]:25.17e}')


# root関数(2)
#final = sopt.root(func, [x0, y0], jac = dfunc)

# Jacobi行列生成
#jacobi = dfunc(x0)
jacobi = dfunc_ag(x0)
print('jacobi(x0) = ', jacobi)

final = sopt.root(func, x0, jac = dfunc_ag)

# 表示
print('最終 -> x =')
for i in range(0, (final.x).size):
	print(f'{i:3d}, {final.x[i]:25.17e}')

print('検算 -> f(x) = ')
for i in range(0, (final.fun).size):
	print(f'{i:3d}, {final.fun[i]:25.17e}')

