# ode_epidemic.py: 常微分方程式の初期値問題

# numpy
import numpy as np

# integrateパッケージ
import scipy.integrate as spint

# matplotlib
import matplotlib.pyplot as plt

# 人口 - 11
num_people = 11
# 初期感染者
num_infected_people = 1
# 初期感受性者
num_noninfected_people = num_people - num_infected_people

# 陽的形式の右辺
# y' = func(t, x) = -x(n+1-x)
def func(t, y):
#	return [-y[0] * (num_people - y[0])]
	return np.array([-y[0] * (num_people - y[0]), y[1] * (num_people - y[1])])

# 初期値
# y(0) = [n, 1]
#y0 = [num_noninfected_people]
y0 = [num_noninfected_people, num_infected_people]

# t = [0, 1]
t_interval = [0.0, 1.0]
#print(t_interval)

# 常微分方程式を解く(1)
#ret = spint.solve_ivp(func, t_interval, y0)
ret = spint.solve_ivp(func, t_interval, y0, t_eval = np.linspace(t_interval[0], t_interval[1], 100))

# 感染者の増加率を計算
w = [num_noninfected_people] # 初期感染者発生率
for index in range(1, ret.t.size):
    w.append((ret.y[1, index] - ret.y[1, index - 1]) / (ret.t[index] - ret.t[index - 1]))

# 結果を表示
#print(ret)
#print('w = ', w)

# yを表示
#print(ret.y)

# t-yグラフを描画
# グラフ初期化
figure, axis = plt.subplots()

# 値をセット
axis.plot(ret.t, ret.y[0, :], label='x(u)')
axis.plot(ret.t, ret.y[1, :], label='y(u)')
axis.plot(ret.t, w, label='w(u)')

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel = 't', ylabel = 'y', title = 'Epidemic model')

# グリッドを描画
axis.grid()

# 凡例
axis.legend()

# グラフ保存ファイル名
figure.savefig('ode_epidemic.png')

# グラフを画面に描画
plt.show()
