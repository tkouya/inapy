# quadratic_eq_mpmath.py: 2次方程式を解く(gmpy2版)
from gmpy2 import *

# 128 bits
get_context().precision = 128

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = mpfr(a), mpfr(b), mpfr(c)
print(' ', a, ' * x^2')
print('+', b, ' * x')
print('+', c, ' = 0')

# 判別式
d = b ** 2 - 4 * a * c

# 実数解: d >= 0
x1 = (-b + sqrt(d)) / (2 * a)
x2 = (-b - sqrt(d)) / (2 * a)

# 出力
print('x1 = ', x1)
print('x2 = ', x2)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
