# 自動微分
import autograd.numpy as np
import autograd # as npdiff
import matplotlib.pyplot as plt

def func(x):
	return x ** 2 # x^2

def true_dfunc(x):
	return 2 * x #

# x = [-5, 5]
x = np.linspace(-5, 5, 100)

# 自動微分による導関数
dfunc = autograd.elementwise_grad(func)
#dfunc = true_dfunc

# 相対誤差チェック
reldiff = np.abs((dfunc(x) - true_dfunc(x)) / true_dfunc(x))
print('reldiff = ', reldiff)

# グラフ初期化
# figure, axis = matplotlib.pyplot.subplots()
figure, axis = plt.subplots()
axis.plot(x, func(x), x, dfunc(x))
axis.set(xlabel = 'x', ylabel = 'y', title = 'y = sin(x) and sin\'(x)')
axis.grid()
figure.savefig('sin.png')
plt.show()
