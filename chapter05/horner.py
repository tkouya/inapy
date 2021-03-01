# horner.py: ホーナー法
# NumPy多項式poly1dと比較
import numpy as np


# ホーナー法
def horner_poly(x, coef):
    deg = len(coef)  # deg = 次数 - 1
    ret = coef[0]
    for i in range(0, deg - 1):
        ret = ret * x + coef[i + 1]

    return ret


# p(x) = (-4) * x^3 + 3 * x^2 + (-2) * x + 1
poly_coef = [-4.0, 3.0, -2.0, 1.0]
print('poly_coef = ', poly_coef)

# numpy.poly1d
p = np.poly1d(poly_coef)
print('p(x) = \n', p)

# x = sqrt(3)
x = np.sqrt(3.0)
print('horner p(', x, ') = ', horner_poly(x, poly_coef))
print('Numpy  p(', x, ') = ', p(x))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
