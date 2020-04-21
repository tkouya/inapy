# runge_phenominon.py: Rungeの現象
import numpy as np # NumPy
import scipy as sc # SciPy
import matplotlib.pyplot as plt # Matpllotlib

# l_k(x) = (x - x[0]) * ... * (x - x[n-1]) / (x[k] - x[0]) * ... * (x[k] - x[n-1])
def poly_lk(k, x_array):
    n = x_array.size
    ret_poly = 1.0
    for i in range(k):
#        print(np.poly1d([1.0, x_array[i]]))
        ret_poly *= np.poly1d([1.0, -x_array[i]]) / (x_array[k] - x_array[i])
    for i in range(k + 1, n):
        ret_poly *= np.poly1d([1.0, -x_array[i]]) / (x_array[k] - x_array[i])

    return ret_poly

# Lagrange補間多項式
def lagrange_poly(x_array, y_array):
    n = x_array.size
    ret_poly = 0.0
    for i in range(n):
        ret_poly += poly_lk(i, x_array) * y_array[i]
    
    return ret_poly

# B(x)
def B_lagrange_poly(x, x_array, y_array):
    n = x_array.size
    ret = 0.0
    for i in range(n):
        val_poly_lk = (poly_lk(i, x_array))(x)
        ret += np.abs(val_poly_lk * y_array[i])
   
    return ret

# 真の関数
def org_func(x):
    return 1.0 / (1.0 + 25.0 * x ** 2)

# [a, b]
min_x, max_x = -1.0, 1.0

# num_div
num_div = 10
x_array = np.linspace(min_x, max_x, num_div)

# y_array = org_func(x_array)
y_array = np.array([org_func(x_array[i]) for i in range(x_array.size)])

print('x_array = ', x_array)
print('y_array = ', y_array)

# 多項式補間
interpoly = lagrange_poly(x_array, y_array)

print('interpoly = ')
print(interpoly(x_array))

print('B(x) = ')
print([B_lagrange_poly(x_array[i], x_array, y_array) for i in range(x_array.size)])

# グラフ描画
kinds_x = 5
x = []
B_array = []
for i in range(kinds_x):
    x.append(np.linspace(min_x, max_x, num_div * 10 * (i + 1)))
    B_array.append([B_lagrange_poly(x[i][j], x_array, y_array) for j in range(x[i].size)])
    print('x[', i, '] = ', x[i])
    print('B[', i, '] = ', B_array[i])

fig, ax = plt.subplots()
for i in range(kinds_x):
    ax.plot(x[i], B_array[i])

ax.set(xlabel = 'x', ylabel = 'B(x)', title = 'Runge\' Phenomenon')
ax.grid()

fig.savefig('runge.png')

