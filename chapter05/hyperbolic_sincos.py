# hyperbolic_sincos.py: 双曲線関数
import math  # sinh(x), cosh(x), tanh(x)
import numpy as np

# relerr関数
from tktools import relerr


# 定義に基づくsinh(x)
def mysinh(x):
    return (math.exp(x) - math.exp(-x)) / 2.0


# 定義に基づくcosh(x)
def mycosh(x):
    return (math.exp(x) + math.exp(-x)) / 2.0


# 定義に基づくtanh(x)
def mytanh(x):
    return mysinh(x) / mycosh(x)


# Maclaurin展開に基づくsinh(x)
def maclaurin_sinh(x, rtol, atol, max_deg):
    old_ret = x
    ret = old_ret
    xn = x
    coef = 1.0  # = 0!
    for i in range(3, max_deg, 2):
        coef /= (i - 1) * i  # coef = 1/i!
        xn *= x**2  # xn = x^n
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret, i
        old_ret = ret

    return ret, i


# Maclaurin展開に基づくcosh(x)
def maclaurin_cosh(x, rtol, atol, max_deg):
    old_ret = 1.0
    ret = old_ret
    xn = 1.0
    coef = 1.0  # = 0!
    for i in range(2, max_deg, 2):
        coef /= (i - 1) * i  # coef = 1/i!
        xn *= x**2  # xn = x^n
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret, i
        old_ret = ret

    return ret, i


rtol = 1.0e-15
atol = 1.0e-50
max_deg = 1000
x_array = np.linspace(0.1, 10, num=10)  # [1, 10]
maclaurin_val = [0, 0]
math_val = [0, 0, 0]
deg = [0, 0]
reldiff = [0, 0, 0, 0, 0]

print('                  maclaurin_sinh(x), cosh(x)     , mysinh(x),  mycosh(x),  mytanh(x)')
print('     x    , relerr[0] , relerr[1] ,deg[0],deg[1],  relerr[2],  relerr[3],  relerr[4]')
for x in x_array:
    maclaurin_val[0], deg[0] = maclaurin_sinh(x, rtol, atol, max_deg)
    maclaurin_val[1], deg[1] = maclaurin_cosh(x, rtol, atol, max_deg)
    math_val[0] = math.sinh(x)
    math_val[1] = math.cosh(x)
    math_val[2] = math.tanh(x)

    reldiff[0] = relerr(maclaurin_val[0], math_val[0])
    reldiff[1] = relerr(maclaurin_val[1], math_val[1])
    reldiff[2] = relerr(mysinh(x), math_val[0])
    reldiff[3] = relerr(mycosh(x), math_val[1])
    reldiff[4] = relerr(mytanh(x), math_val[2])

    print(f'{x:10.3e}, {reldiff[0]:10.3e}, {reldiff[1]:10.3e}, {deg[0]:5d}, {deg[1]:5d}, {reldiff[2]:10.3e}, {reldiff[3]:10.3e}, {reldiff[4]:10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
