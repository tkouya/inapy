# integration_simple2.py: 台形公式，Simpsonの1/3公式，Gauss型積分公式による数値積分
# + 改良台形公式
import numpy as np
from tktools import relerr # relerr

# 台形公式
def trapezoidal_int(int_func, min_x, max_x, num_div):
    # 積分区間刻み幅
    h = (max_x - min_x) / num_div

    # 区間内離散点と関数評価
    in_x = np.array([min_x + h * i for i in range(1, num_div)])
    ret = np.sum(int_func(in_x)) + 0.5 * (int_func(min_x) + int_func(max_x))
    ret *= h

    return ret


# 改良台形公式
def modtrapezoidal_int(int_func, min_x, max_x, num_div):
    # 積分区間刻み幅
    h = (max_x - min_x) / num_div

    # 区間内離散点と関数評価
    in_x = np.array([min_x + h * i for i in range(1, num_div)])
    ret = np.sum(int_func(in_x)) + 0.5 * (int_func(min_x) + int_func(max_x))

    # 改良部分
    ret += 1.0 / 24.0 * (-int_func(min_x - h) + int_func(min_x + h) + int_func(max_x - h) - int_func(max_x + h))

    ret *= h

    return ret


# Simpsonの1/3公式
def simpson13_int(int_func, min_x, max_x, num_div):

    # 区間は偶数とする
    if num_div % 2 != 0: num_div += 1
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
def get_x(a, b, t):
    return (b - a) / 2 * t + (b + a) / 2 


# Gauss型積分公式:2点公式を繰り返し使用
def gauss2_int(int_func, min_x, max_x, num_div):

    # 積分区間分割
    h = (max_x - min_x) / num_div
    in_x = np.array([min_x + h * i for i in range(num_div + 1)]) # 端点含む

    # 分点と重み
    abscissa = np.array([
        -0.577350269189625764509148780501, 
        0.577350269189625764509148780501
    ])
    weight   = np.array([1.0, 1.0])

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
    in_x = np.array([min_x + h * i for i in range(num_div + 1)]) # 端点含む

    # 分点と重み
    abscissa = np.array([
        -0.774596669241483377035853079956,
        0.0,
        0.774596669241483377035853079956
    ])
    weight   = np.array([
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


# Gauss型積分公式:4点公式を繰り返し使用
def gauss4_int(int_func, min_x, max_x, num_div):

    # 積分区間分割
    h = (max_x - min_x) / num_div
    in_x = np.array([min_x + h * i for i in range(num_div + 1)]) # 端点含む

    # 分点と重み
    abscissa = np.array([
        -0.861136311594052575223946488892,
        -0.339981043584856264802665759103,
        +0.339981043584856264802665759103,
        +0.861136311594052575223946488892
    ])
    weight   = np.array([
        0.347854845137453857373063949221,
        0.652145154862546142626936050778,
        0.652145154862546142626936050778,
        0.347854845137453857373063949221
    ])

    # 区間ごとに変数変換
    ret = 0.0
    for i in range(num_div):
        in_in_x = get_x(in_x[i], in_x[i + 1], abscissa)
        ret += np.sum(int_func(in_in_x) * weight)

    ret *= (max_x - min_x) / 2 / num_div

    return ret


# 問題12.4
def func1(x):
	return 5 * np.sqrt(1 - 0.8**2 * x**2) / np.sqrt(1 - x**2)


# 問題12.5
def func2(x):
    return np.sin(x)


# 問題2.5真値
def true_integral2(a, b):
    return -np.cos(b) + np.cos(a)


# 演習問題2
def func3(x):
    return np.log(x)


# 演習問題2真値
def true_integral3(a, b):
    return (b * np.log(b) - b) - (a * np.log(a) - a) 


# 問題12.4
print('\nProblem 12.4')
a, b = 0, 4/5
print('Trapezoidal    : ', trapezoidal_int(func1, a, b, 4))
print('Simpson13      : ', simpson13_int(func1, a, b, 4))

# 問題12.5
print('\nProblem 12.5')
a, b = 0, np.pi
gval2 = gauss2_int(func2, a, b, 1)
gval3 = gauss3_int(func2, a, b, 1)
gval4 = gauss4_int(func2, a, b, 1)
true_val = true_integral2(a, b)
print('gauss2, relerr : ', gval2, relerr(gval2, true_val))
print('gauss3, relerr : ', gval3, relerr(gval3, true_val))
print('gauss4, relerr : ', gval4, relerr(gval4, true_val))

# 演習問題2
print('\nExercise 2')
a, b = 1, 2
trap = trapezoidal_int(func3, a, b, 4)
simp = simpson13_int(func3, a, b, 4)
gval4 = gauss4_int(func3, a, b, 1)
true_val = true_integral3(a, b)
print('Trapezoidal, relerr : ', trap,  relerr(trap, true_val))
print('Simpson13  , relerr : ', simp,  relerr(simp, true_val))
print('gauss4     , relerr : ', gval4, relerr(gval4, true_val))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
