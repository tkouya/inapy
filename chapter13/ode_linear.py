# ode_linear.py: 常微分方程式の初期値問題
# 硬くない(nonstiff)線型常微分方程式と硬い(stiff)線型常微分方程式
import numpy as np # NumPy
import scipy.integrate as spint # ODEintパッケージ
import time # 時間計測

# Non-stiff
def nonstiff_func(t, y):
	z = [
		-2.0 * y[0] + y[1] - np.cos(t),
		2.0 * y[0] - 3.0 * y[1] + 3.0 * np.cos(t) - np.sin(t)
	]
	return z


# Stiff
def stiff_func(t, y):
	z = [
		-2.0 * y[0] + y[1] - np.cos(t),
		1998.0 * y[0] - 1999.0 * y[1] + 1999.0 * np.cos(t) - np.sin(t)
	]
	return z


# 解析解
def ans(t):
    return [np.exp(-t), np.exp(-t) + np.cos(-t)]


# 初期値
y0 = [1.0, 2.0]

# t = [0, 20]
t_interval = [0.0, 20.0]
print(t_interval)

# 常微分方程式を解く

# RK45
# Nonstiff
stime = time.time()
ret_nonstiff = spint.solve_ivp(nonstiff_func, t_interval, y0, method = 'RK45', rtol = 1.0e-3, atol = 0.0)
time_ret_nonstiff = time.time() - stime

# Stiff
stime = time.time()
ret_stiff = spint.solve_ivp(stiff_func, t_interval, y0, method = 'RK45')
time_ret_stiff = time.time() - stime

# Radau IIA
# Nonstiff
stime = time.time()
ret_radau_nonstiff  = spint.solve_ivp(nonstiff_func, t_interval, y0, method = 'Radau')
time_ret_radau_nonstiff = time.time() - stime

# Stiff
stime = time.time()
ret_radau_stiff  = spint.solve_ivp(stiff_func, t_interval, y0, method = 'Radau')
time_ret_radau_stiff = time.time() - stime

# 計算時間と総ステップ数
print('ret_nonstiff time, #steps = ', time_ret_nonstiff, ret_nonstiff.t.size)
print('time_ret_stiff            = ', time_ret_stiff, ret_stiff.t.size)
print('time_ret_radau_nonstiff   = ', time_ret_radau_nonstiff, ret_radau_nonstiff.t.size)
print('time_ret_radau_stiff      = ', time_ret_radau_stiff, ret_radau_stiff.t.size)

# 相対誤差
true_y = ans(ret_nonstiff.t); relerr_ret_nonstiff = np.abs((ret_nonstiff.y - true_y) / true_y)
true_y = ans(ret_stiff.t); relerr_ret_stiff = np.abs((ret_stiff.y - true_y) / true_y)

true_y = ans(ret_radau_nonstiff.t); relerr_ret_nonstiff_radau = np.abs((ret_radau_nonstiff.y - true_y) / true_y)
true_y = ans(ret_radau_stiff.t); relerr_ret_stiff_radau = np.abs((ret_radau_stiff.y - true_y) / true_y)

# tとyの表示
print('t_end_nonstiff =', ret_nonstiff.t[-1])
print('y_end_nonstiff =', ret_nonstiff.y[0, -1], ret_nonstiff.y[1, -1])
print('relerr_nonstiff=', relerr_ret_nonstiff[0, -1], relerr_ret_nonstiff[1, -1])
print('t_end_stiff    =', ret_stiff.t[-1])
print('y_end_stiff    =', ret_stiff.y[0, -1], ret_stiff.y[1, -1])
print('relerr_nonstiff=', relerr_ret_stiff[0, -1], relerr_ret_stiff[1, -1])

print('t_end_nonstiff_radau =', ret_radau_nonstiff.t[-1])
print('y_end_nonstiff_radau =', ret_radau_nonstiff.y[0, -1], ret_nonstiff.y[1, -1])
print('relerr_nonstiff_radau=', relerr_ret_nonstiff_radau[0, -1], relerr_ret_nonstiff_radau[1, -1])
print('t_end_stiff_radau    =', ret_radau_stiff.t[-1])
print('y_end_stiff_radau    =', ret_radau_stiff.y[0, -1], ret_stiff.y[1, -1])
print('relerr_stiff_radau   =', relerr_ret_stiff_radau[0, -1], relerr_ret_stiff_radau[1, -1])


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
