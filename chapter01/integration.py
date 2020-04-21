# T.Kouya's Python3
import numpy as np

k = 4.0 / 5.0

# 被積分関数
def func(x):
	return 5 * np.sqrt(1 - k**2 * x**2) / np.sqrt(1 - x**2)

# 近似定積分
def integration(x_start, x_end, function, num_div):

	ret = 0
	h = (x_end - x_start) / num_div
	x = x_start
	x_next = x + h

	for i in range(0, num_div - 1):
		ret += function((x + x_next) / 2) * h
		x = x_next
		x_next = x + h

	return ret

# 定積分
a, b, n = 0, k, 100
ret = integration(a, b, func, n)

print('integral[', a, ', ', b, '] : ', ret)
