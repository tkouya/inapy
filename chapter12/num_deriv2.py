# num_deriv2.py: 演習問題1
import numpy as np

# 相対誤差
def relerr(approx, true_val):
	relerr_val = np.abs(approx - true_val)
	if true_val != 0: relerr_val /= np.abs(true_val)

	return relerr_val


# 元の関数
def org_func(x):
	return np.sin(np.cos(x))


# 1階導関数
def diff_func(x):
	return np.cos(np.cos(x)) * (-np.sin(x))


# 前進差分商 : (func(x + h) - func(x)) / h
def forward_diff(func, x, h):
    return (func(x + h) - func(x)) / h


# 後退差分商 : (func(x) - func(x - h)) / h
def backward_diff(func, x, h):
    return (func(x) - func(x - h)) / h


# 中心差分商: (func(x + 0.5 * h) - func(x - 0.5 * h)) / h
def central_diff(func, x, h):
    return (func(x + 0.5 * h) - func(x - 0.5 * h)) / h


# 真の微分係数 
x = np.pi / 4.0
true_deriv = diff_func(x)
print('真値                 = ', diff_func(x))

# h = 10^(-3)
fderiv = forward_diff(org_func, x, 10**(-3))  # 前進差分商
bderiv = backward_diff(org_func, x, 10**(-3))  # 後退差分商
cderiv = central_diff(org_func, x, 10**(-1))
print(f'{x:10.3e}, {relerr(fderiv, true_deriv):10.3e}, {relerr(bderiv, true_deriv):10.3e}, {relerr(cderiv, true_deriv):10.3e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
