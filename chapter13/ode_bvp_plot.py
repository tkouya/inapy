# ODE境界値問題
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_bvp.html#scipy.integrate.solve_bvp
import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt

# Bulirsch & Store
def func(x, y):
	return np.vstack((y[1], 400 * y[0] + 400 * (np.cos(np.pi * x))**2 + 2 * np.pi** 2 * np.cos(2 * np.pi * x)))

# 境界条件
def boundary_condition(y_left, y_right):
	return np.array([y_left[0], y_right[0]])

# 真の解
def true_sol(x):
	return (np.exp(-20) / (1 + np.exp(-20))) * np.exp(20 * x) + (1 / (1 + np.exp(-20))) * np.exp(-20 * x) - (np.cos(np.pi * x)) ** 2

# [a, b] = [0, 1]
div = 10
x  = np.linspace(0, 1, div)
x2 = np.linspace(0, 1, div * 50)
print('[a, b] = [', x[0], x[-1], ']')

# 境界値を設定
y  = np.zeros((2, x.size))
y2 = np.zeros((2, x2.size))

# 境界値問題を解く
res  = scint.solve_bvp(func, boundary_condition, x, y, verbose = 2)
res2 = scint.solve_bvp(func, boundary_condition, x2, y2)

print('x   = ', res.x)
print('sol = ', res.y[0])
print('sol2 = ', res2.y[0])

true_y = true_sol(res.x)
relerr_x = res.x
relerr_y = np.abs(np.divide(res.y[0] - true_y, true_y))
#print('relerr = ', relerr_y)

true_y2 = true_sol(res2.x)
relerr_x = res2.x
relerr_y2 = np.abs(np.divide(res2.y[0] - true_y2, true_y2))

# 解を描画
x_plot = np.linspace(0, 1, div * 10) # 10倍の解像度
y_plot = res.sol(x_plot)[0] # 密出力(数値解を補間)
y_plot2 = res2.sol(x_plot)[0]

plt.figure(1)

plt.subplot(211) # 1段目
plt.plot(x_plot, y_plot, label='y')
#plt.plot(x_plot, y_plot2, label='y')
plt.legend()
plt.grid()
#plt.xlabel('x')
plt.ylabel('y')

plt.subplot(212) # 2段目
plt.plot(res.x, relerr_y, label='Initial ' + str(res.x.size) + ' points')
plt.plot(res2.x, relerr_y2, label='Initial ' + str(res2.x.size) + ' points')
#plt.legend(loc = 'upper left')
plt.legend(loc = 'upper left', bbox_to_anchor=(0.07, 0.95))
plt.grid()
plt.xlabel('x')
plt.ylabel('Relative Error')
plt.yscale('log')

# グラフ保存ファイル名
plt.savefig('ode_bvp.png')

# グラフを画面に描画
#plt.show()
