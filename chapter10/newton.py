# newton.py: Newton法
import numpy as np

# f(x) = 0
def func(x):
    return x - np.cos(x)


# f'(x) = 0
def dfunc(x):
    return 1 + np.sin(x)


# 初期値
x0 = 1.0

# 停止条件
atol = 1.0e-50
rtol = 1.0e-10

# Newton反復
x_old = x0
for times in range(0, 100):
    x_new = x_old - func(x_old) / dfunc(x_old)
#    print(f'x_{times:d} = {x_new:25.17e}')
    print(f'x_{times:d} = {x_new:25.17e}, {func(x_new):10.3e}')
    if np.abs(x_new - x_old) <= rtol * np.abs(x_old) + atol:
        break
    x_old = x_new

# 表示
print(f'最終 -> x_{times:d} = {x_new:25.17e}')
print(f'検算 -> func(x_{times:d}) = {func(x_new):25.17e}')

