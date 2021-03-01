# np_calc.py: NumPyの初等関数機能
import numpy as np  # NumPy
import math  # mathモジュール
import cmath  # cmathモジュール

a = -3.0
z = -1.0 + 2.0j

print('a = ', a)
print('z = ', z)

# 平方根: NumPy
print('np.sqrt(a) = ', np.sqrt(a))
print('np.sqrt(z) = ', np.sqrt(z))

# 平方根: math, cmath
# print('math.sqrt(a) = ', math.sqrt(a))  # エラーになる
print('cmath.sqrt(z) = ', cmath.sqrt(z))

# べき乗: NumPy
c = np.sqrt(a)
w = np.sqrt(z)
print('(np.sqrt(a))^2 = ', c ** 2)
print('(np.sqrt(z))^2 = ', w ** 2)

# べき乗: math
# c = math.sqrt(a) #エラーになる
w = cmath.sqrt(z)
# print('(math.sqrt(a))^2 = ', c ** 2)
print('(cmath.sqrt(z))^2 = ', w ** 2)

# 指数関数，三角関数，対数関数: NumPy
print('np.exp(a)   = ', np.exp(a))
print('np.sin(a)   = ', np.sin(a))
print('np.log(a)   = ', np.log(a))
print('np.log10(a) = ', np.log10(a))
print('np.exp(z)   = ', np.exp(z))
print('np.sin(z)   = ', np.sin(z))
print('np.log(z)   = ', np.log(z))
print('np.log10(z) = ', np.log10(z))

# 指数関数，三角関数，対数関数: math
print('math.exp(a)   = ', math.exp(a))
print('math.sin(a)   = ', math.sin(a))
# print('math.log(a)   = ', math.log(a))  # エラーになる
# print('math.log10(a) = ', math.log10(a))  # エラーになる
print('cmath.exp(z)   = ', cmath.exp(z))
print('cmath.sin(z)   = ', cmath.sin(z))
print('cmath.log(z)   = ', cmath.log(z))
print('cmath.log10(z) = ', cmath.log10(z))

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
