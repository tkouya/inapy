# autograd_diff.py: 自動微分
import autograd.numpy as np
import autograd


# 元の関数
def func(x):
	return np.exp(np.cos(x)) - x ** 3


# 真の導関数
def true_dfunc(x):
	return -np.exp(np.cos(x)) * np.sin(x) - 3 * x ** 2


# x = [-5, 5]
x = np.linspace(-5, 5, 100)

# 自動微分による導関数
dfunc = autograd.elementwise_grad(func)

# 相対誤差チェック
reldiff = np.abs((dfunc(x) - true_dfunc(x)) / true_dfunc(x))
print('reldiff = ', reldiff)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
