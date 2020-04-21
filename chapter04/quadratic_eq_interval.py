# quadratic_eq_interval.py: 2次方程式を解く
from interval import *

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = Interval(float(a)), Interval(float(b)), Interval(float(c))
print(' ', a, ' * x^2')
print('+', b, ' * x')
print('+', c, ' = 0')


# 判別式
d = b ** 2 - 4 * a * c
print('d = ', d)

# 実数解: d >= 0
x1 = (-b + d.sqrt()) / (2 * a)
x2 = (-b - d.sqrt()) / (2 * a)

# 出力
print('x1 = ', x1)
print('x2 = ', x2)

