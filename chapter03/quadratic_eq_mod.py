# quadratic_eq_mod.py: 2次方程式を解く(改良版)
import math  # sqrt関数

# 係数入力
a = input('a =? ')
b = input('b =? ')
c = input('c =? ')
a, b, c = float(a), float(b), float(c)
print(f'  {a:25.17g} * x^2')
print(f'+ {b:25.17g} * x')
print(f'+ {c:25.17g} = 0')

# 判別式
d = b ** 2 - 4 * a * c

# 実数解: d >= 0
if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    # 出力
    print(f'x1  = {x1:25.17e}')
    print(f'x2  = {x2:25.17e}')

    # 改良版
    if b >= 0.0:
        sign_b = 1.0
    else:
        sign_b = -1.0

    x1d = (-b - sign_b * math.sqrt(d)) / (2 * a)
    x2d = c / (a * x1d)

    # 出力
    print(f'x1d = {x1d:25.17e}')
    print(f'x2d = {x2d:25.17e}')

    # 検算
    print('a * x1 ^2 + b * x1  + c =? ', a * x1**2 + b * x1 + c)
    print('a * x2 ^2 + b * x2  + c =? ', a * x2**2 + b * x2 + c)
    print('a * x1d^2 + b * x1d + c =? ', a * x1d**2 + b * x1d + c)
    print('a * x2d^2 + b * x2d + c =? ', a * x2d**2 + b * x2d + c)

else:  # 複素数解
    print("Complex !")


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
