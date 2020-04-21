# Newton法
import numpy as np
import scipy.optimize as sopt

# f(x) = 0
def func(x):
	return x - np.cos(x)
#	return (x - 3) ** 3

# f'(x) = 0
def dfunc(x):
	return 1 + np.sin(x)
#	return np.array([3 * (x - 3) ** 2])

# 初期値
x0 = 1.0

# root関数(1)
final = sopt.root(func, x0)

# 表示
print(f'最終 -> x = {final.x[0]:25.17e}')
print(f'検算 -> func(x) = {final.fun[0]:25.17e}')


# root関数(2)
final = sopt.root(func, x0, jac = dfunc)

# 表示
print(f'最終 -> x = {final.x[0]:25.17e}')
print(f'検算 -> func(x) = {final.fun[0]:25.17e}')

