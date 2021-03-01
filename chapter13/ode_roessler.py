# 常微分方程式の初期値問題

# numpy
import numpy as np

# ODEintパッケージ
import scipy.integrate as spint

# matplotlib
import matplotlib as mp
import matplotlib.pyplot as plt

# sys
import sys

# 陽的形式の右辺
alpha = 1.0 / 5.0
beta = 1.0 / 5.0
#mu = 3
#mu = 4
mu = 5 # Chaos
# y' = func(t, y)

def func(t, y):
	z = [
		-(y[1] + y[2]),
        y[0] + alpha * y[1],
		beta + y[2] * (y[0] - mu)
	]
	return z

# 初期値
y0 = [1.0, 0.0, 0.0]

# t = [0, 500]を0.1刻みで
t_interval = [0.0, 500.0]
t_all = np.arange(t_interval[0], t_interval[1], 0.1)
print(t_interval)

# 常微分方程式を解く
ret = spint.solve_ivp(func, t_interval, y0, t_eval = t_all)
ret_rk45   = spint.solve_ivp(func, t_interval, y0, method = 'RK45', t_eval = t_all)
ret_rk23   = spint.solve_ivp(func, t_interval, y0, method = 'RK23',t_eval = t_all)
#ret_dop853 = spint.solve_ivp(func, t_interval, y0, method = 'DOP853',t_eval = t_all)
ret_radau  = spint.solve_ivp(func, t_interval, y0, method = 'Radau', t_eval = t_all)
ret_bdf    = spint.solve_ivp(func, t_interval, y0, method = 'BDF', t_eval = t_all)
ret_lsoda  = spint.solve_ivp(func, t_interval, y0, method = 'LSODA', t_eval = t_all)

# yを表示
#print(ret.y)

# t-yグラフを描画
# グラフ初期化
# figure, axis = matplotlib.pyplot.subplots()
figure, axis = plt.subplots()

# 値をセット
#axis.plot(t, y1)
#axis.plot(t, y2)
print(ret.y)
#axis.plot(ret.y[0, :], ret.y[1, :])
axis.plot(ret_rk45.y[0, :], ret_rk45.y[1, :])
#axis.plot(ret_rk23.y[0, :], ret_rk23.y[1, :])
#axis.plot(ret_radau.y[0, :], ret_radau.y[1, :])
#axis.plot(ret_bdf.y[0, :], ret_bdf.y[1, :])
#axis.plot(ret_lsoda.y[0, :], ret_lsoda.y[1, :])

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel = 'x', ylabel = 'y', title = 'Roessler Model(mu = ' + str(mu) + '): RK45')

# グリッドを描画
axis.grid()

# グラフ保存ファイル名
figure.savefig(__file__ + '.png')

# グラフを画面に描画
# matplotlib.pyplot.show()
plt.show()


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
