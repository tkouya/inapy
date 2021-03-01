# integration_simple.py: 台形公式，Simpsonの1/3公式，Gauss型積分公式による数値積分
import numpy as np


# 台形公式
def trapezoidal_int(int_func, min_x, max_x, num_div):
    # 積分区間刻み幅
    h = (max_x - min_x) / num_div

    # 区間内離散点と関数評価
    in_x = np.array([min_x + h * i for i in range(1, num_div)])
    ret = np.sum(int_func(in_x)) + 0.5 * (int_func(min_x) + int_func(max_x))
    ret *= h

    return ret


# Simpsonの1/3公式
def simpson13_int(int_func, min_x, max_x, num_div):

    # 区間は偶数とする
    if num_div % 2 != 0:
        num_div += 1
    half_num_div = int(num_div / 2)

    # 積分区間刻み幅
    h = (max_x - min_x) / num_div

    # 区間内離散点と関数評価
    in_x_odd = np.array([min_x + h * (2 * i - 1) for i in range(1, half_num_div + 1)])
    in_x_even = np.array([min_x + h * (2 * i) for i in range(1, half_num_div)])

    ret = 4.0 * np.sum(int_func(in_x_odd)) + 2.0 * np.sum(int_func(in_x_even)) + (int_func(min_x) + int_func(max_x))
    ret *= h / 3.0

    return ret


# Gauss型積分公式用の変数変換
def get_x(a, b, t): return (b - a) / 2 * t + (b + a) / 2


# Gauss型積分公式:2点公式を繰り返し使用
def gauss2_int(int_func, min_x, max_x, num_div):

    # 積分区間分割
    h = (max_x - min_x) / num_div
    in_x = np.array([min_x + h * i for i in range(num_div + 1)])  # 端点含む

    # 分点と重み
    abscissa = np.array([
        -0.577350269189625764509148780501,
        0.577350269189625764509148780501
    ])
    weight = np.array([1.0, 1.0])

    # 区間ごとに変数変換
    ret = 0.0
    for i in range(num_div):
        in_in_x = get_x(in_x[i], in_x[i + 1], abscissa)
        ret += np.sum(int_func(in_in_x) * weight)

    ret *= (max_x - min_x) / 2 / num_div

    return ret


# Gauss型積分公式:3点公式を繰り返し使用
def gauss3_int(int_func, min_x, max_x, num_div):

    # 積分区間分割
    h = (max_x - min_x) / num_div
    in_x = np.array([min_x + h * i for i in range(num_div + 1)])  # 端点含む

    # 分点と重み
    abscissa = np.array([
        -0.774596669241483377035853079956,
        0.0,
        0.774596669241483377035853079956
    ])
    weight = np.array([
        0.555555555555555555555555555555,
        0.888888888888888888888888888888,
        0.555555555555555555555555555555
    ])

    # 区間ごとに変数変換
    ret = 0.0
    for i in range(num_div):
        in_in_x = get_x(in_x[i], in_x[i + 1], abscissa)
        ret += np.sum(int_func(in_in_x) * weight)

    ret *= (max_x - min_x) / 2 / num_div

    return ret


# 被積分関数
def func(x):
    return x ** (-2)


# 定積分
a, b = 1.0, 2.0

print('Trapezoidal : ', trapezoidal_int(func, a, b, 1))
print('gauss2      : ', gauss2_int(func, a, b, 1))
print('Simpson13   : ', simpson13_int(func, a, b, 2))
print('gauss3      : ', gauss3_int(func, a, b, 1))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
