# maclaurin_sin.py: Maclaurin展開に基づく初等関数計算(sin(x), cos(x))
import math
import numpy as np

# relerr関数
from tktools import relerr


# Maclaurin展開に基づくsin(x)
def maclaurin_sin_org(x, rtol, atol, max_deg):
    old_ret = x
    ret = old_ret
    xn = x
    coef = 1.0  # = 1!
    for i in range(3, max_deg, 2):
        coef /= (i - 1) * i  # coef = 1/i!
        coef *= -1.0
        xn *= x**2  # xn = x^n
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret, i
        old_ret = ret

    return ret, i


# Maclaurin展開に基づくsin(x) : 区間判定
def maclaurin_sin(x, rtol, atol, max_deg):

    ret_val, i = np.nan, 0

    # sin(|x|)の計算を行う
    abs_x = np.abs(x)

    # |x| > 2 * pi
    if abs_x > 2 * np.pi:
        abs_x -= 2.0 * np.pi * np.floor(abs_x / (2.0 * np.pi))

    # abs_x == 0.0, pi
    if (abs_x == 0.0) or (abs_x == np.pi):
        ret_val, i = 0.0, 0
    # abs_x == pi / 2
    elif (abs_x == np.pi / 2) or (abs_x == np.pi * 2):
        ret_val, i = 1.0, 0
    # abs_x in (0, pi/2)
    elif (abs_x > 0.0) and (abs_x < np.pi / 2):
        ret_val, i = maclaurin_sin_org(abs_x, rtol, atol, max_deg)
    # abs_x in (pi/2, pi)
    elif (abs_x > np.pi / 2) and (abs_x < np.pi):
        tmp_abs_x = np.pi - abs_x
        ret_val, i = maclaurin_sin_org(tmp_abs_x, rtol, atol, max_deg)
    # abs_x in (pi, 2 * pi)
    elif (abs_x > np.pi) and (abs_x < 2 * np.pi):
        tmp_abs_x = abs_x - np.pi
        ret_val, i = maclaurin_sin_org(tmp_abs_x, rtol, atol, max_deg)
        ret_val = -ret_val

    # x < 0
    if x < 0:
        ret_val = -ret_val

    return ret_val, i


# Maclaurin展開に基づくcos(x)
def maclaurin_cos_org(x, rtol, atol, max_deg):
    old_ret = 1.0
    ret = old_ret
    xn = 1.0
    coef = 1.0  # = 0!
    for i in range(2, max_deg, 2):
        coef /= (i - 1) * i  # coef = 1/i!
        coef *= -1.0
        xn *= x**2  # xn = x^n
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret, i
        old_ret = ret

    return ret, i


# Maclaurin展開に基づくcos(x) : 区間判定
def maclaurin_cos(x, rtol, atol, max_deg):

    ret_val, i = np.nan, 0

    # cos(|x|)の計算を行う
    abs_x = np.abs(x)

    # |x| > 2 * pi
    if abs_x > 2 * np.pi:
        abs_x -= 2.0 * np.pi * np.floor(abs_x / (2.0 * np.pi))

    # abs_x == 0.0 or 2 * pi
    if (abs_x == 0.0) or (abs_x == 2.0 * np.pi):
        ret_val, i = 1.0, 0
    # abs_x == pi
    elif (abs_x == np.pi):
        ret_val, i = -1.0, 0
    # abs_x == pi / 2 or 3 * pi / 2
    elif (abs_x == np.pi / 2) or (abs_x == 1.5 * np.pi):
        ret_val, i = 0.0, 0
    # abs_x in (0, pi/2)
    elif (abs_x > 0.0) and (abs_x < np.pi / 2):
        ret_val, i = maclaurin_cos_org(abs_x, rtol, atol, max_deg)
    # abs_x in (pi/2, (3/2) * pi)
    elif (abs_x > np.pi / 2) and (abs_x < np.pi):
        tmp_abs_x = np.pi - x
        ret_val, i = maclaurin_cos_org(tmp_abs_x, rtol, atol, max_deg)
        ret_val = -ret_val
    # abs_x in (pi, 2 * pi)
    elif (abs_x > np.pi) and (abs_x < 2 * np.pi):
        tmp_abs_x = abs_x - np.pi
        ret_val, i = maclaurin_cos_org(tmp_abs_x, rtol, atol, max_deg)
        ret_val = -ret_val

    return ret_val, i


rtol = 1.0e-15
atol = 0.0
max_deg = 1000
x_array = np.linspace(-10, 10, num=10)  # [-10, 10]
maclaurin_val = [0, 0]
deg = [0, 0]
reldiff = [0, 0]

print('                    sin(x)               cos(x)')
print('     x    ,  relerr[0], deg[0], relerr[1], deg[1]')
for x in x_array:
    # sin(x)
    maclaurin_val[0], deg[0] = maclaurin_sin(x, rtol, atol, max_deg)
    math_val = math.sin(x)  # math.sin
    reldiff[0] = relerr(maclaurin_val[0], math_val)

    # cos(x)
    maclaurin_val[1], deg[1] = maclaurin_cos(x, rtol, atol, max_deg)
    math_val = math.cos(x)  # math.cos
    reldiff[1] = relerr(maclaurin_val[1], math_val)

    print(f'{x:10.3e}, {reldiff[0]:10.3e}, {deg[0]:5d}, {reldiff[1]:10.3e}, {deg[1]:5d}')

x = 1.5
print('x = 1.5')
# sin(1.5)
maclaurin_val[0], deg[0] = maclaurin_sin(x, rtol, atol, max_deg)
math_val = math.sin(x)  # math.sin
reldiff[0] = relerr(maclaurin_val[0], math_val)

# cos(1.5)
maclaurin_val[1], deg[1] = maclaurin_cos(x, rtol, atol, max_deg)
math_val = math.cos(x)  # math.cos
reldiff[1] = relerr(maclaurin_val[1], math_val)

print(f'{x:10.3e}, {reldiff[0]:10.3e}, {deg[0]:5d}, {reldiff[1]:10.3e}, {deg[1]:5d}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
