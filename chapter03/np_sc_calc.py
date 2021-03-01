# np_sc_calc.py: NumPyとSciPy
import numpy as np  # NumPy
import numpy.matlib as npmat
import scipy.special as scspf  # SciPy.specialパッケージ

# relerr : 相対誤差
from tktools import relerr  # tktools.py: 私的作成関数

n = 10

# 乱数の種セット
np.random.seed(n)

# n個の乱数セット
a = npmat.rand(n)

print('a = ', a)

# 立方根
sc_c = scspf.cbrt(a)  # SciPy.special
np_c = np.cbrt(a)  # NumPy

# 相対誤差の最大値と最小値
relerr_vec = relerr(sc_c, np_c)
print('max(reldiff(sc_c, np_c)) = ', np.max(relerr_vec))
print('min(reldiff(sc_c, np_c)) = ', np.min(relerr_vec))

# expm1(a) = exp(a) - 1
sc_c = scspf.expm1(a)
np_c = np.exp(a) - 1

print('SciPy expm1(a) = ', sc_c)
print('NumPy exp(a)-1 = ', np_c)

# 相対誤差の最大値と最小値
relerr_vec = relerr(sc_c, np_c)
print('max(reldiff(sc_c, np_c)) = ', np.max(relerr_vec))
print('min(reldiff(sc_c, np_c)) = ', np.min(relerr_vec))

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
