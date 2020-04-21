# 常微分方程式の初期値問題

# numpy
import numpy as np

# matplotlib
import matplotlib as mp
import matplotlib.pyplot as plt

# ODEintパッケージ
from scipy.integrate import odeint
# Linear Algebraパッケージ
#from scipy import linalg

# sys
import sys

# 陽的形式の右辺
a = 2
b = 3
c = 1
d = 2
# y' = func(y, t)
def func(y, t):
	z = [
		(a - b * y[1]) * y[0],
		(-c + d * y[0]) * y[1]
	]
	return z

# 初期値
# y(0) = (c/d + 0.1, a/b + 0.1)
y01 = [c/d + 0.1, a/b + 0.1]
# y(0) = (c/d + 1, a/b + 1)
y02 = [c/d + 1, a/b + 1]

# t = [0, 50]を0.1刻みで
t = np.arange(0, 50, 0.1)

# 常微分方程式を解く
y1 = odeint(func, y01, t)
y2 = odeint(func, y02, t)

# yを表示
#print(y1)
#print(y2)

# t-yグラフを描画
# グラフ初期化
# figure, axis = matplotlib.pyplot.subplots()
figure, axis = plt.subplots()

# 値をセット
#axis.plot(t, y1)
#axis.plot(t, y2)
axis.plot(y1[:, 0], y1[:, 1])
axis.plot(y2[:, 0], y2[:, 1])

# x軸，y軸，グラフタイトルをセット
#axis.set(xlabel = 't', ylabel = 'y', title = 'Lotka-Volterra')
axis.set(xlabel = 'y_1', ylabel = 'y_2', title = 'Lotka-Volterra')

# グリッドを描画
axis.grid()

# グラフ保存ファイル名
figure.savefig(__file__ + '.png')

# グラフを画面に描画
# matplotlib.pyplot.show()
plt.show()
