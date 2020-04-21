# 自動微分
import autograd.numpy as np
import autograd # as npdiff
import matplotlib.pyplot as plt

def func(x):
	#	return x ** 2 # x^2
	return np.sin(x)

def true_dfunc(x):
	#	return 2 * x #
	return np.cos(x)

dfunc = autograd.elementwise_grad(func)

# x = [-5, 5]
#x = np.linspace(-5, 5, 100)
# x = [-pi, pi]
x = np.linspace(0, np.pi, 100)

# 自動微分による導関数
def dfunc_line(func, dfunc, x, x0):
	return dfunc(x0) * (x - x0) + func(x0)

# グラフ初期化
# figure, axis = matplotlib.pyplot.subplots()
figure, axis = plt.subplots()
axis.plot(x, func(x))
for x0 in x:
	axis.plot(x, dfunc_line(func, dfunc, x, x0))

axis.set(xlabel = 'x', ylabel = 'y', title = 'y = sin(x) and sin\'(x)')
axis.grid()
figure.savefig('sin2.png')
plt.show()
