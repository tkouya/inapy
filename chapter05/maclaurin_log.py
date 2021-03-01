# maclaurin_log.py: Maclaurin展開に基づく初等関数計算
import math
import numpy as np

# relerr関数
from tktools import relerr


# mylog(x) : 展開式1
def _mylog1(x, rtol, atol, max_deg):
    in_x = (x - 1.0) / (x + 1.0)
    old_ret = in_x
    ret = old_ret
    xn = in_x
    coef = 1.0  # = 1!
    for i in range(3, max_deg, 2):
        coef = 1.0 / i  # coef = 1/i
        xn *= in_x ** 2  # xn = x^n
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret * 2, i
        old_ret = ret

    return ret * 2, i


# mylog2(x) : 展開式2
def _mylog2(x, rtol, atol, max_deg):
    in_x = (x - 1.0) / x
    old_ret = in_x
    ret = old_ret
    xn = in_x
    coef = 1.0  # = 1!
    for i in range(2, max_deg):
        coef = 1.0 / i  # coef = 1/i
        xn *= in_x  # xn = x^n
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret, i
        old_ret = ret

    return ret, i


# mylog(x): 区間判定
def mylog(x, rtol, atol, max_deg, maclaurin_log):

    ret_val, i = np.nan, 0
    flag_minus = 0  # そのまま返す
    flag_deg_e = 0  # exp(n)を掛ける
    deg_e = 0  # * e^deg_e
    in_exp = 2.7182818284590452353602874713527

    in_x = x

    # 負数には対応しない
    if x < 0.0:
        return ret_val, i

    # x in (0, 1)
    if (x > 0.0) and (x < 1.0):
        in_x = 1.0 / x
        flag_minus = 1  # 符号反転

    # e^n < x < e^(n + 1)
    if in_x > in_exp:
        in_exp_deg = in_exp
        in_exp_degp1 = in_exp * in_exp
        for deg in range(1, 710):  # e^709 = 8.28... * 10^307
            if(in_x > in_exp_deg) and (in_x <= in_exp_degp1):
                deg_e = deg
                flag_deg_e = 1  # exp(deg_e)を掛ける
                in_x /= in_exp_deg
                break
            in_exp_deg = in_exp_degp1
            in_exp_degp1 *= in_exp

    # in_x == 1
    if in_x == 1.0:
        ret_val = 0.0
    elif (in_x > 1.0) and (in_x < in_exp):
        ret_val, i = maclaurin_log(in_x, rtol, atol, max_deg)
    elif in_x == in_exp:
        ret_val = 1.0

    # flag処理
    if flag_deg_e == 1:
        ret_val += deg_e  # log(in_x * exp^deg_e)
    if flag_minus == 1:
        ret_val = -ret_val  # log(1/x)

    return ret_val, i


rtol = 1.0e-15
atol = 0.0
max_deg = 1000
x_array = np.linspace(0.1, 10, num=10)  # [1, 10]
maclaurin_val = [0, 0]
deg = [0, 0]
reldiff = [0, 0]

print('     x    , relerr[0] , relerr[1] , deg[0], deg[1]')
for x in x_array:
    # 手製log関数1
    maclaurin_val[0], deg[0] = mylog(x, rtol, atol, max_deg, _mylog1)
    # 手製log関数2
    maclaurin_val[1], deg[1] = mylog(x, rtol, atol, max_deg, _mylog2)
    math_val = math.log(x)  # math.log

    reldiff[0] = relerr(maclaurin_val[0], math_val)
    reldiff[1] = relerr(maclaurin_val[1], math_val)

    print(f'{x:10.3e}, {reldiff[0]:10.3e}, {reldiff[1]:10.3e}, {deg[0]:5d}, {deg[1]:5d}')

# x = 100
x = 100
print('x = %g' % x)
maclaurin_val[0], deg[0] = mylog(x, rtol, atol, max_deg, _mylog1)
maclaurin_val[1], deg[1] = mylog(x, rtol, atol, max_deg, _mylog2)
math_val = math.log(x)  # math.log

reldiff[0] = relerr(maclaurin_val[0], math_val)
reldiff[1] = relerr(maclaurin_val[1], math_val)

print(f'{x:10.3e}, {reldiff[0]:10.3e}, {reldiff[1]:10.3e}, {deg[0]:5d}, {deg[1]:5d}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
