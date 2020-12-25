# ode_sir.py: SIRモデル
# 解説文書 -> https://www.orsj.or.jp/archive2/or56-12/or56-12_728.pdf
import numpy as np
# ODEintパッケージ
import scipy.integrate as scint
# グラフ描画ライブラリ
# matplotlib
import matplotlib as mp
import matplotlib.pyplot as plt

# 総人口
n = 1000

# 初期感染者数 > 0
i0 = 1

# 初期回復者数
r0 = 1

# 初期感染予備群数
s0 = n - (i0 + r0) # 総人口 S + I + R = n

# 平均感染期間 inv_a = 1 / a
inv_a = 10 # 日数
a = 1.0 / float(inv_a)

# 伝達係数
r = 0.01 # 感染力 = r * I(t)

# y' = func(y, t)
def func(y0, t0):
    y = [
        -r * y0[0] * y0[1],  # S
         r * y0[0] * y0[1] - a * y0[1],  # I
         a * y0[1]  # R
    ]
    return y

# 初期値
y0 = np.array([s0, i0, r0])

# t = [0, 50]を0.001刻みで
t = np.arange(0, 50, 0.001)

#print('t = ', t)

# 常微分方程式を解く
y1 = scint.odeint(func, y0, t)

# t-yグラフを描画
figure, axis = plt.subplots()

# 値をセット
axis.plot(t, y1[:, 0], label='S(t)')
axis.plot(t, y1[:, 1], label='I(t)')
axis.plot(t, y1[:, 2], label='R(t)')

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel = 't', ylabel = 'y', title = 'SIR model: ' + 'r = ' + str(r) + ', 1/a = ' + str(1/a) + '\n y0 = ' + str(y0) + '')

# グリッドを描画
axis.grid()

# 凡例
axis.legend()

# グラフ保存ファイル名
#figure.savefig('sir.png')

# グラフ表示
plt.show()
