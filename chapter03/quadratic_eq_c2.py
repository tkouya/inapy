# quadratic_eq_c2.py: 2次方程式を解く(複素係数対応)
import cmath  # sqrt関数

# 係数入力
re_a = input('Re(a) =? ')
im_a = input('Im(a) =? ')
re_b = input('Re(b) =? ')
im_b = input('Im(b) =? ')
re_c = input('Re(c) =? ')
im_c = input('Im(c) = ?')
a = float(re_a) + float(im_a) * 1j
b = float(re_b) + float(im_b) * 1j
c = float(re_c) + float(im_c) * 1j
print(f'  {a:25.17g} * x^2')
print(f'+ {b:25.17g} * x')
print(f'+ {c:25.17g} = 0')

# 解の計算
d = b**2 - 4 * a * c
x1 = (-b + cmath.sqrt(d)) / (2 * a)
x2 = (-b - cmath.sqrt(d)) / (2 * a)

# 出力
print(f'x1 = {x1:25.17e}')
print(f'x2 = {x2:25.17e}')

# 検算
print('a * x1^2 + b * x1 + c = ', a * x1**2 + b * x1 + c)
print('a * x2^2 + b * x2 + c = ', a * x2**2 + b * x2 + c)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
