# ode_bvp.py : ODE境界値問題
import numpy as np
import scipy.integrate as scint

# Bulirsch & Store
def func(x, y):
	return np.vstack((y[1], 400 * y[0] + 400 * (np.cos(np.pi * x))**2 + 2 * np.pi** 2 * np.cos(2 * np.pi * x)))

# 境界条件
def boundary_condition(y_left, y_right):
	return np.array([y_left[0], y_right[0]])

# 真の解
def true_sol(x):
	return (np.exp(-20) / (1 + np.exp(-20))) * np.exp(20 * x) + (1 / (1 + np.exp(-20))) * np.exp(-20 * x) - (np.cos(np.pi * x)) ** 2

# [a, b] = [0, 1]
div = 10  # div : x方向分割数 
div2 = div * 50 # 上記の50倍の分割数
x  = np.linspace(0, 1, div)
x2 = np.linspace(0, 1, div2)
print('[a, b] = [', x[0], x[-1], ']')

# 境界値を設定
y  = np.zeros((2, x.size))
y2 = np.zeros((2, x2.size))

# 境界値問題を解く
res  = scint.solve_bvp(func, boundary_condition, x, y, verbose = 2)
res2 = scint.solve_bvp(func, boundary_condition, x2, y2)

print('x   = ', res.x)
print('sol = ', res.y[0])
print('sol2 = ', res2.y[0])

true_y = true_sol(res.x)
relerr_x = res.x
relerr_y = np.abs(np.divide(res.y[0] - true_y, true_y))
print('div = ', div)
print('relerr = ', relerr_y)

true_y2 = true_sol(res2.x)
relerr_x = res2.x
relerr_y2 = np.abs(np.divide(res2.y[0] - true_y2, true_y2))
print('relerr2 = ', relerr_y2)
