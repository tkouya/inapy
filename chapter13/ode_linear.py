# 常微分方程式の初期値問題

# numpy
import numpy as np

# ODEintパッケージ
import scipy.integrate as spint

# matplotlib
import matplotlib.pyplot as plt

# 時間計測
import time

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

# t = [0, 20]を2^(-p)刻みで
t_interval = [0.0, 20.0]
p = 2
t_all = np.arange(t_interval[0], t_interval[1], 1.0 / 2 ** p)
print(t_interval)

# 常微分方程式を解く
# Nonstiff
stime = time.time()
ret_nonstiff = spint.solve_ivp(nonstiff_func, t_interval, y0)
time_ret_nonstiff = time.time() - stime

# Stiff
stime = time.time()
ret_stiff = spint.solve_ivp(stiff_func, t_interval, y0)
time_ret_stiff = time.time() - stime
#ret_rk45   = spint.solve_ivp(func, t_interval, y0, method = 'RK45', t_eval = t_all)
#ret_rk23   = spint.solve_ivp(func, t_interval, y0, method = 'RK23',t_eval = t_all)
#ret_dop853 = spint.solve_ivp(func, t_interval, y0, method = 'DOP853',t_eval = t_all)

# Nonstiff
stime = time.time()
ret_radau_nonstiff  = spint.solve_ivp(nonstiff_func, t_interval, y0, method = 'Radau')
time_ret_radau_nonstiff = time.time() - stime

# Stiff
stime = time.time()
ret_radau_stiff  = spint.solve_ivp(stiff_func, t_interval, y0, method = 'Radau')
time_ret_radau_stiff = time.time() - stime
#ret_bdf    = spint.solve_ivp(func, t_interval, y0, method = 'BDF', t_eval = t_all)
#ret_lsoda  = spint.solve_ivp(func, t_interval, y0, method = 'LSODA', t_eval = t_all)

# yを表示
print('ret_nonstiff time, #steps = ', time_ret_nonstiff, ret_nonstiff.t.size)
print('time_ret_stiff    = ', time_ret_stiff, ret_stiff.t.size)
print('time_ret_radau_nonstiff = ', time_ret_radau_nonstiff, ret_radau_nonstiff.t.size)
print('time_ret_radau_stiff    = ', time_ret_radau_stiff, ret_radau_stiff.t.size)

# 相対誤差
true_y = ans(ret_nonstiff.t); relerr_ret_nonstiff = np.abs((ret_nonstiff.y - true_y) / true_y)
true_y = ans(ret_stiff.t); relerr_ret_stiff = np.abs((ret_stiff.y - true_y) / true_y)

true_y = ans(ret_radau_nonstiff.t); relerr_ret_nonstiff_radau = np.abs((ret_radau_nonstiff.y - true_y) / true_y)
true_y = ans(ret_radau_stiff.t); relerr_ret_stiff_radau = np.abs((ret_radau_stiff.y - true_y) / true_y)

# 相対誤差のグラフ描画
# グラフ初期化
# figure, axis = matplotlib.pyplot.subplots()
figure, axis = plt.subplots(nrows = 2, ncols = 2)

# １列目 -- Nonstiff Problem
axis[0, 0].set_yscale('log') # log10スケール
axis[0, 0].plot(ret_nonstiff.t, relerr_ret_nonstiff[0, :], label='RK45')
axis[0, 0].plot(ret_radau_nonstiff.t, relerr_ret_nonstiff_radau[0, :], label='Radau')
axis[0, 0].set(ylabel = 'Relative Error of y1', title = 'Nonstiff Problem')
axis[0, 0].grid(True)
axis[0, 0].legend()

axis[1, 0].set_yscale('log') # log10スケール
axis[1, 0].plot(ret_nonstiff.t, relerr_ret_nonstiff[1, :], label='RK45')
axis[1, 0].plot(ret_radau_nonstiff.t, relerr_ret_nonstiff_radau[1, :], label='Radau')
axis[1, 0].set(xlabel = 't', ylabel = 'Relative Error of y2')
axis[1, 0].grid(True)
axis[1, 0].legend()

# 2列目 --- Stiff Problem
axis[0, 1].set_yscale('log') # log10スケール
axis[0, 1].plot(ret_stiff.t, relerr_ret_stiff[0, :], label='RK45')
axis[0, 1].plot(ret_radau_stiff.t, relerr_ret_stiff_radau[0, :], label='Radau')
axis[0, 1].set(ylabel = 'Relative Error of y1', title = 'Stiff Problem')
axis[0, 1].grid(True)
axis[0, 1].legend()

axis[1, 1].set_yscale('log') # log10スケール
axis[1, 1].plot(ret_stiff.t, relerr_ret_stiff[1, :], label='RK45')
axis[1, 1].plot(ret_radau_stiff.t, relerr_ret_stiff_radau[1, :], label='Radau')
axis[1, 1].set(xlabel = 't', ylabel = 'Relative Error of y2')
axis[1, 1].grid(True)
axis[1, 1].legend()

# グラフ保存ファイル名
plt.savefig(__file__ + '.png')

# グラフを画面に描画
# matplotlib.pyplot.show()
plt.show()
