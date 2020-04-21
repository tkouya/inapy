# quadratic_eq_iv.py: 2次方程式を解く
from mpmath import iv

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = iv.mpf(a), iv.mpf(b), iv.mpf(c)
print(' ', a, ' * x^2')
print('+', b, ' * x')
print('+', c, ' = 0')

# 判別式
d = b ** 2 - 4 * a * c

# 実数解: d >= 0
x1 = (-b + iv.sqrt(d)) / (2 * a)
x2 = (-b - iv.sqrt(d)) / (2 * a)

# 出力
print('x1 = ', x1)
print('x2 = ', x2)

