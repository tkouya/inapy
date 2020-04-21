# interpoly.py: 多項式補間
import numpy as np
import scipy as spy
import scipy.linalg as slinalg
import scipy.interpolate as sipl

# 大本の関数
def org_func(x):
	return np.sin(x)
#	return 1 / (x**2 + 1)

# 補間点数
str_n = input('補間点数を入力 n = ')
n = int(str_n)

# 補間点
x = np.zeros(n)
y = np.zeros(n)
print('x.size = ', x.size)
for i in range(0, n):
	print('補間点xを入力 x[', i ,'] = ')
	str_x = input()
	x[i] = float(str_x)
	y[i] = org_func(x[i])

print('x = ', x)
print('y = ', y)

# Vandermonde行列生成
v_mat = np.zeros((n, n))
for i in range(0, n):
	for j in range(0, n):
		v_mat[i, j] = x[i] ** j

print('V = '); print(v_mat)

# new_y := V^(^1) * y
v_coef = slinalg.inv(v_mat) @ y
print('v_coef = ', np.flip(v_coef))

# Lagrange補間
l_poly = sipl.lagrange(x, y)
print('l_coef = ', l_poly.coef)

# Kroph補間
k_poly = sipl.KroghInterpolator(x, y)
print('k(x) = ', k_poly(x))
print('k\'(x) = ', k_poly.derivative(x, der=1))
print('k\'\'(x) = ', k_poly.derivative(x, der=2))
