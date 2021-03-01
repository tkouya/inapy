# integration_scipy.py: 数値積分による定積分+問題12.4
import numpy as np
import scipy.integrate as scint  # 積分パッケージ


# 被積分関数
def func1(x, k):
    return 5 * np.sqrt(1 - k ** 2 * x ** 2) / np.sqrt(1 - x ** 2)


# 定積分
k = 4 / 5
a, b = 0, k
ret = scint.quad(func1, a, b, args=(k))

print('integral[', a, ', ', b, '] : ', ret[0])
print('ret = ', ret)
print('aE(ans)              = ', ret[1])
print('rE(ans)              = ', np.abs(ret[1] / ret[0]))


# 被積分関数
def func1(x):
	return np.log(np.abs(x))


def func2(x):
	return np.exp(-x)


def func3(x):
	return x ** (-1/2)


# 定積分1
a, b = 0.0, 1.0
ret = scint.quad(func1, a, b)

print('integral[', a, ', ', b, '] : ', 2.0 * ret[0])
print('ret = ', ret)
print('aE(ans)              = ', ret[1])
print('rE(ans)              = ', np.abs(ret[1] / ret[0]))

# 定積分2
a, b = 0.0, np.inf
ret = scint.quad(func2, a, b)

print('integral[', a, ', ', b, '] : ', ret[0])
print('ret = ', ret)
print('aE(ans)              = ', ret[1])
print('rE(ans)              = ', np.abs(ret[1] / ret[0]))

# 定積分3
a, b = 0.0, 1.0
ret = scint.quad(func3, a, b)

print('integral[', a, ', ', b, '] : ', ret[0])
print('ret = ', ret)
print('aE(ans)              = ', ret[1])
print('rE(ans)              = ', np.abs(ret[1] / ret[0]))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
