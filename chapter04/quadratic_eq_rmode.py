# quadratic_eq_rmode.py: 2次方程式を解く
import rmode
from math import *

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = float(a), float(b), float(c)
print(' ', a, ' * x^2')
print('+', b, ' * x')
print('+', c, ' = 0')

# RN_RM
rmode.set_rmode(rmode.FE_DOWNWARD)

# 判別式
d = b ** 2 - 4 * a * c

# 実数解: d >= 0
x1_rm = (-b + sqrt(d)) / (2 * a)
x2_rm = (-b - sqrt(d)) / (2 * a)

# RN_RP
rmode.set_rmode(rmode.FE_UPWARD)
d = b ** 2 - 4 * a * c
x1_rp = (-b + sqrt(d)) / (2 * a)
x2_rp = (-b - sqrt(d)) / (2 * a)

# RN_RN
rmode.set_rmode(rmode.FE_TONEAREST)
d = b ** 2 - 4 * a * c
x1_rn = (-b + sqrt(d)) / (2 * a)
x2_rn = (-b - sqrt(d)) / (2 * a)

# 出力
print('x1 = ', x1_rm, x1_rn, x1_rp)
print('x2 = ', x2_rm, x2_rn, x2_rp)
print('|x1_rn - x1_rp|/|x1_rn| = ', abs(x1_rn - x1_rp) / abs(x1_rn))
print('|x1_rn - x1_rm|/|x1_rn| = ', abs(x1_rn - x1_rm) / abs(x1_rn))
print('|x2_rn - x2_rp|/|x2_rn| = ', abs(x2_rn - x2_rp) / abs(x2_rn))
print('|x2_rn - x2_rm|/|x2_rn| = ', abs(x2_rn - x2_rm) / abs(x2_rn))
