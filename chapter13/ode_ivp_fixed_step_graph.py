# ode_fixed_step.py: 常微分方程式の初期値問題(固定刻み幅)
# euler    : Euler法
# mid_point: 中点法
# erk44    : 古典的Runge-Kutta法
# erk76    : 陽的Runge-Kutta法(7段6次)

# numpy
import numpy as np

# matplotlib
import matplotlib.pyplot as plt

# Euler法
def euler(t_end, ode_func, t0, y0, max_num_div):

    old_t = t0
    old_y = y0
    h = (t_end - t0) / max_num_div

    t = [t0]
    y = [y0]

    # メインループ
    for num_step in range(max_num_div):
        new_t = old_t + h

        # Euler法
        new_y = old_y + h * ode_func(old_t, old_y)

        old_t = new_t
        old_y = new_y

        t.append(old_t)
        y.append(old_y)

    return t, y
        
# 中点法
def mid_point(t_end, ode_func, t0, y0, max_num_div):

    old_t = [0.0, 0.0]
    old_y = [y0, y0]

    old_t[0] = t0
    old_y[0] = y0
    h = (t_end - t0) / max_num_div

    # 最初はEuler法
    old_t[1] = old_t[0] + h
    old_y[1] = old_y[0] + h * ode_func(old_t[0], old_y[0])

    t = [old_t[0], old_t[1]]
    y = [old_y[0], old_y[1]]

    # メインループ
    for num_step in range(1, max_num_div):
        new_t = old_t[1] + h

        # 中点法
        new_y = old_y[0] + 2 * h * ode_func(old_t[1], old_y[1])

        old_t[0] = old_t[1]
        old_y[0] = old_y[1]
        old_t[1] = new_t
        old_y[1] = new_y

        t.append(old_t[1])
        y.append(old_y[1])

    return t, y

# (s, e) := QuickTwoSum(a, b) if |a| > |b|
def quick_two_sum(a, b):
    s = a + b
    w = s - a
    e = b - w

    return s, e


# 古典的Runge-Kutta法
def erk44(t_end, ode_func, t0, y0, max_num_div):

    old_t = t0
    hk = [y0, y0, y0, y0] # hk[i] := h * k[i]
    old_y = y0

    t = [t0]
    y = [y0]

    h = (t_end - t0) / max_num_div

    # メインループ
    for num_step in range(max_num_div):
        new_t = old_t + h

        # k[0]～k[3]の計算
        hk[0] = h * ode_func(old_t, old_y)
        hk[1] = h * ode_func(old_t + 0.5 * h, old_y + 0.5 * hk[0])
        hk[2] = h * ode_func(old_t + 0.5 * h, old_y + 0.5 * hk[1])
        hk[3] = h * ode_func(old_t +       h, old_y +       hk[2])

        # 陽的Runge-Kutta法
        new_y = old_y + (hk[0] + 2 * hk[1] + 2 * hk[2] + hk[3]) / 6.0

        old_t = new_t
        old_y = new_y

        t.append(old_t)
        y.append(old_y)

    return t, y

# 古典的Runge-Kutta法
def erk44m(t_end, ode_func, t0, y0, max_num_div):

    old_t = t0
    hk = [y0, y0, y0, y0] # hk[i] := h * k[i]
    old_y = y0

    # 丸め誤差蓄積用
    temp_hy = y0
    ochibo = np.zeros(y0.shape)

    t = [t0]
    y = [y0]

    h = (t_end - t0) / max_num_div

    # メインループ
    for num_step in range(max_num_div):
        new_t = old_t + h

        # k[0]～k[3]の計算
        hk[0] = h * ode_func(old_t, old_y)
        hk[1] = h * ode_func(old_t + 0.5 * h, old_y + 0.5 * hk[0])
        hk[2] = h * ode_func(old_t + 0.5 * h, old_y + 0.5 * hk[1])
        hk[3] = h * ode_func(old_t +       h, old_y +       hk[2])

        # 陽的Runge-Kutta法
        temp_hy = (hk[0] + 2 * hk[1] + 2 * hk[2] + hk[3]) / 6.0 + ochibo
        new_y, ochibo = quick_two_sum(old_y, temp_hy)

        old_t = new_t
        old_y = new_y

        t.append(old_t)
        y.append(old_y)

    return t, y

# 陽的Runge-Kutta法: 7段6次のButcher公式
def erk76(t_end, ode_func, t0, y0, max_num_div):

    # 係数初期化
    c = [1.0/3.0, 2.0/3.0, 1.0/3.0, 1.0/2.0, 1.0/2.0, 1.0]
    a = [
        [1.0/3.0  , 0.0      ,  0.0     , 0.0      , 0.0    , 0.0       ],
        [0.0      , 2.0/3.0  ,  0.0     , 0.0      , 0.0    , 0.0       ],
        [1.0/12.0 , 1.0/3.0  , -1.0/12.0, 0.0      , 0.0    , 0.0       ],
        [-1.0/16.0, 9.0/8.0  , -3.0/16.0, -3.0/8.0 , 0.0    , 0.0       ],
        [0.0      , 9.0/8.0  , -3.0/8.0 , -3.0/4.0 , 1.0/2.0, 0.0       ],
        [9.0/44.0 , -9.0/11.0, 63.0/44.0, 18.0/11.0, 0.0    , -16.0/11.0]
    ]
    w = [11.0/120.0, 0.0, 27.0/40.0, 27.0/40.0, -4.0/15.0, -4.0/15.0, 11.0/120.0]

    old_t = t0
    hk = [y0, y0, y0, y0, y0, y0, y0] # hk[i] := h * k[i]
    old_y = y0

    t = [t0]
    y = [y0]

    h = (t_end - t0) / max_num_div

    # メインループ
    for num_step in range(max_num_div):
        new_t = old_t + h

        # k[0]～k[6]の計算
        hk[0] = h * ode_func(old_t, old_y)
        hk[1] = h * ode_func(old_t + c[0] * h, old_y + a[0][0] * hk[0])
        hk[2] = h * ode_func(old_t + c[1] * h, old_y + a[1][0] * hk[0] + a[1][1] * hk[1])
        hk[3] = h * ode_func(old_t + c[2] * h, old_y + a[2][0] * hk[0] + a[2][1] * hk[1] + a[2][2] * hk[2])
        hk[4] = h * ode_func(old_t + c[3] * h, old_y + a[3][0] * hk[0] + a[3][1] * hk[1] + a[3][2] * hk[2] + a[3][3] * hk[3])
        hk[5] = h * ode_func(old_t + c[4] * h, old_y + a[4][0] * hk[0] + a[4][1] * hk[1] + a[4][2] * hk[2] + a[4][3] * hk[3] + a[4][4] * hk[4])
        hk[6] = h * ode_func(old_t + c[5] * h, old_y + a[5][0] * hk[0] + a[5][1] * hk[1] + a[5][2] * hk[2] + a[5][3] * hk[3] + a[5][4] * hk[4] + a[5][5] * hk[5])

        # 陽的Runge-Kutta法
        new_y = old_y + (w[0] * hk[0] + w[1] * hk[1] + w[2] * hk[2] + w[3] * hk[3] + w[4] * hk[4] + w[5] * hk[5] + w[6] * hk[6])

        old_t = new_t
        old_y = new_y

        t.append(old_t)
        y.append(old_y)

    return t, y

# 陽的Runge-Kutta法: 7段6次のButcher公式
def erk76m(t_end, ode_func, t0, y0, max_num_div):

    # 係数初期化
    c = [1.0/3.0, 2.0/3.0, 1.0/3.0, 1.0/2.0, 1.0/2.0, 1.0]
    a = [
        [1.0/3.0  , 0.0      ,  0.0     , 0.0      , 0.0    , 0.0       ],
        [0.0      , 2.0/3.0  ,  0.0     , 0.0      , 0.0    , 0.0       ],
        [1.0/12.0 , 1.0/3.0  , -1.0/12.0, 0.0      , 0.0    , 0.0       ],
        [-1.0/16.0, 9.0/8.0  , -3.0/16.0, -3.0/8.0 , 0.0    , 0.0       ],
        [0.0      , 9.0/8.0  , -3.0/8.0 , -3.0/4.0 , 1.0/2.0, 0.0       ],
        [9.0/44.0 , -9.0/11.0, 63.0/44.0, 18.0/11.0, 0.0    , -16.0/11.0]
    ]
    w = [11.0/120.0, 0.0, 27.0/40.0, 27.0/40.0, -4.0/15.0, -4.0/15.0, 11.0/120.0]

    old_t = t0
    hk = [y0, y0, y0, y0, y0, y0, y0] # hk[i] := h * k[i]
    old_y = y0

    # 丸め誤差蓄積用
    temp_hy = y0
    ochibo = np.zeros(y0.shape)

    t = [t0]
    y = [y0]

    h = (t_end - t0) / max_num_div

    # メインループ
    for num_step in range(max_num_div):
        new_t = old_t + h

        # k[0]～k[6]の計算
        hk[0] = h * ode_func(old_t, old_y)
        hk[1] = h * ode_func(old_t + c[0] * h, old_y + a[0][0] * hk[0])
        hk[2] = h * ode_func(old_t + c[1] * h, old_y + a[1][0] * hk[0] + a[1][1] * hk[1])
        hk[3] = h * ode_func(old_t + c[2] * h, old_y + a[2][0] * hk[0] + a[2][1] * hk[1] + a[2][2] * hk[2])
        hk[4] = h * ode_func(old_t + c[3] * h, old_y + a[3][0] * hk[0] + a[3][1] * hk[1] + a[3][2] * hk[2] + a[3][3] * hk[3])
        hk[5] = h * ode_func(old_t + c[4] * h, old_y + a[4][0] * hk[0] + a[4][1] * hk[1] + a[4][2] * hk[2] + a[4][3] * hk[3] + a[4][4] * hk[4])
        hk[6] = h * ode_func(old_t + c[5] * h, old_y + a[5][0] * hk[0] + a[5][1] * hk[1] + a[5][2] * hk[2] + a[5][3] * hk[3] + a[5][4] * hk[4] + a[5][5] * hk[5])

        # 陽的Runge-Kutta法
#        new_y = old_y + (w[0] * hk[0] + w[1] * hk[1] + w[2] * hk[2] + w[3] * hk[3] + w[4] * hk[4] + w[5] * hk[5] + w[6] * hk[6])
        temp_hy = (w[0] * hk[0] + w[1] * hk[1] + w[2] * hk[2] + w[3] * hk[3] + w[4] * hk[4] + w[5] * hk[5] + w[6] * hk[6]) + ochibo
        new_y, ochibo = quick_two_sum(old_y, temp_hy)

        old_t = new_t
        old_y = new_y

        t.append(old_t)
        y.append(old_y)

    return t, y

# 陽的形式の右辺
# y' = func(t, y)
def func(t, y):
#    ret_y = y
    ret_y = np.array([t + y[0]])
#    ret_y[0] = -2 * y[0] + y[1] - np.cos(t)
#    ret_y[1] = 2 * y[0] - 3 * y[1] + 3 * np.cos(t) - np.sin(t)

    return ret_y

# 真の解
def true_y(t, y0):
#    y = np.array([np.exp(t), np.exp(t)])
    y = np.array([2 * np.exp(t) - 1.0 - t])
    return y

# 成分ごとの相対誤差
def relerr(approx_vec, true_vec):
#    print('approx_vec.size = ', approx_vec.shape)
#    print('true_vec.size   = ', true_vec.shape)
    ret_vec = np.abs((approx_vec - true_vec) / true_vec)
    return ret_vec

# 初期値
# y(0) = 1
y0 = np.array([1.0])
#y0 = np.array([1.0, 1.0])
#y0 = np.array([1.0, 2.0])

# t = [0, 1]
t_interval = [0.0, 1.0]
#t_interval = [0.0, 20.0]
print(t_interval)

# 刻み数と刻み幅
#max_div_t = 10
max_div_t = 10 ** 4
#max_div_t = 10 ** 5

h = (t_interval[1] - t_interval[0]) / max_div_t

# 常微分方程式を解く: Euler法
euler_ret_t, euler_ret_y = euler(t_interval[1], func, t_interval[0], y0, max_div_t)
#print(euler_ret_t, euler_ret_y)
euler_relerr_y = relerr(euler_ret_y, true_y(euler_ret_t, y0).T)

# 常微分方程式を解く: 中点法
mid_point_ret_t, mid_point_ret_y = mid_point(t_interval[1], func, t_interval[0], y0, max_div_t)
mid_point_relerr_y = relerr(mid_point_ret_y, true_y(mid_point_ret_t, y0).T)

# 常微分方程式を解く: 古典的Runge-Kutta法
erk44_ret_t, erk44_ret_y = erk44(t_interval[1], func, t_interval[0], y0, max_div_t)
#print(erk44_ret_t, erk44_ret_y)
erk44_relerr_y = relerr(erk44_ret_y, true_y(erk44_ret_t, y0).T)

# 常微分方程式を解く: 古典的Runge-Kutta法 + Moller法
erk44m_ret_t, erk44m_ret_y = erk44m(t_interval[1], func, t_interval[0], y0, max_div_t)
#print(erk44_ret_t, erk44_ret_y)
erk44m_relerr_y = relerr(erk44m_ret_y, true_y(erk44m_ret_t, y0).T)

# 常微分方程式を解く: 陽的Runge-Kutta法(7段6次)
erk76_ret_t, erk76_ret_y = erk76(t_interval[1], func, t_interval[0], y0, max_div_t)
#print(erk76_ret_t, erk76_ret_y)
erk76_relerr_y = relerr(erk76_ret_y, true_y(erk76_ret_t, y0).T)

# 常微分方程式を解く: 陽的Runge-Kutta法(7段6次) + Moller法
erk76m_ret_t, erk76m_ret_y = erk76m(t_interval[1], func, t_interval[0], y0, max_div_t)
#print(erk76m_ret_t, erk76m_ret_y)
erk76m_relerr_y = relerr(erk76m_ret_y, true_y(erk76m_ret_t, y0).T)

# t-yグラフを描画
# グラフ初期化
figure, axis = plt.subplots()

# 縦軸を対数スケール
axis.set_yscale('log')

# 値をセット
axis.plot(euler_ret_t, euler_relerr_y[:, 0], label='Euler')
axis.plot(mid_point_ret_t, mid_point_relerr_y[:, 0], label='Mid point')
axis.plot(erk44_ret_t, erk44_relerr_y[:, 0], label='ERK44')
axis.plot(erk44m_ret_t, erk44m_relerr_y[:, 0], label='ERK44m')
axis.plot(erk76_ret_t, erk76_relerr_y[:, 0], label='ERK76')
axis.plot(erk76m_ret_t, erk76m_relerr_y[:, 0], label='ERK76m')

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel = 't', ylabel = 'Relative Error of y(0)', title = 'y\' = t + y, h = 1 / ' + str(max_div_t))

# グリッドを描画
axis.grid()

# 凡例
axis.legend()

# グラフ保存ファイル名
figure.savefig('ode_fixed_step.png')

# グラフを画面に描画
plt.show()


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
