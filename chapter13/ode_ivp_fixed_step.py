# ode_ivp_fixed_step.py: 常微分方程式の初期値問題(固定刻み幅)
# euler    : オイラー法
# mid_point: 中点法
# erk44    : 古典的ルンゲ・クッタ法
import numpy as np
from tktools import relerr  # 相対誤差


# オイラー法
def euler(t_end, ode_func, t0, y0, max_num_div):

    old_t = t0
    old_y = y0
    h = (t_end - t0) / max_num_div

    t = [t0]
    y = [y0]

    # メインループ
    for num_step in range(max_num_div):
        new_t = old_t + h

        # オイラー法
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

    # 最初はオイラー法
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


# 古典的ルンゲ・クッタ法
def erk44(t_end, ode_func, t0, y0, max_num_div):

    old_t = t0
    hk = [y0, y0, y0, y0]  # hk[i] := h * k[i]
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

        # 陽的ルンゲ・クッタ法
        new_y = old_y + (hk[0] + 2 * hk[1] + 2 * hk[2] + hk[3]) / 6.0

        old_t = new_t
        old_y = new_y

        t.append(old_t)
        y.append(old_y)

    return t, y


# 陽的形式の右辺
# y' = func(t, y)
def func(t, y):
    ret_y = np.array([t + y[0]])

    return ret_y


# 真の解
def true_y(t, y0):
    y = np.array([2 * np.exp(t) - 1.0 - t])
    return y


# 初期値
# y(0) = 1
y0 = np.array([1.0])

# t = [0, 1]
t_interval = [0.0, 1.0]
print('t in ', t_interval)

# 刻み数と刻み幅
max_div_t = 10

# 常微分方程式を解く: オイラー法
euler_ret_t, euler_ret_y = euler(t_interval[1], func, t_interval[0], y0, max_div_t)
euler_relerr_y = relerr(euler_ret_y, true_y(euler_ret_t, y0).T)

# 常微分方程式を解く: 中点法
mid_point_ret_t, mid_point_ret_y = mid_point(t_interval[1], func, t_interval[0], y0, max_div_t)
mid_point_relerr_y = relerr(mid_point_ret_y, true_y(mid_point_ret_t, y0).T)

# 常微分方程式を解く: 古典的ルンゲ・クッタ法
erk44_ret_t, erk44_ret_y = erk44(t_interval[1], func, t_interval[0], y0, max_div_t)
erk44_relerr_y = relerr(erk44_ret_y, true_y(erk44_ret_t, y0).T)

# 表形式で出力
h = (t_interval[1] - t_interval[0]) / max_div_t
print('h = ', h)
print('                        Relative error of y[0]   ')
print('        t            euler    mid_point     erk44')
for i in range(max_div_t + 1):
    print(f'{t_interval[0] + i * h:15.7e}, {euler_relerr_y[i][0]:10.3e}, {mid_point_relerr_y[i][0]:10.3e}, {erk44_relerr_y[i][0]:10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
