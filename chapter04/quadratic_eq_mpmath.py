# quadratic_eq_mpmath.py: 2次方程式を解く(mpmath版)
from mpmath import *

print('mpmath.libmp.BACKEND = ', libmp.BACKEND)

# 10進40桁計算
mp.dps = 40  # 仮数部の10進桁数

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
print(' ', a, ' * x^2')
print('+', b, ' * x')
print('+', c, ' = 0')

# 判別式
d = b ** 2 - 4 * a * c

# 実数解: d >= 0
x1 = (-b + mp.sqrt(d)) / (2 * a)
x2 = (-b - mp.sqrt(d)) / (2 * a)

# 出力
print('x1 = ', x1)
print('x2 = ', x2)

