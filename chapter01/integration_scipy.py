# T.Kouya's Python3
import numpy as np
import scipy.integrate as scint

k = 4 / 5

# 被積分関数
def func(x, k):
	return 5 * np.sqrt(1 - k**2 * x** 2) / np.sqrt(1 - x**2)

# 定積分
a, b = 0, k
ret = scint.quad(func, a, b, args = (k))

print('integral[', a, ', ', b, '] : ', ret[0])
print('ret = ', ret)
print('aE(ans)              = ', ret[1])
print('rE(ans)              = ', np.abs(ret[1] / ret[0]))
