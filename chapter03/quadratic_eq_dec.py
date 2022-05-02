# quadratic_eq_dec.py: 10進数演算による2次方程式の解法
import decimal as dec # 10進多倍長演算モジュール

# 計算コンテキスト確認
print('current decimal context = ', dec.getcontext())

# 10進5桁計算
dec.getcontext().prec = 5
# 四捨五入
dec.getcontext().rounding = dec.ROUND_HALF_UP

# 計算コンテキスト確認
print('current decimal context = ', dec.getcontext())

# a, b, cを読み込み
a = input('a = ')
b = input('b = ')
c = input('c = ')
a, b, c = dec.Decimal(a), dec.Decimal(b), dec.Decimal(c) # str -> float変換

print('a, b, c = ', a, b, c)

# 判別式計算
d = b * b - dec.Decimal('4.0000') * a * c

# 解の計算と出力(1)
x1 = (-b + d.sqrt()) / (2 * a)
x2 = (-b - d.sqrt()) / (2 * a)
print(f'x1 , x2  = {x1:10.5e}, {x2:10.5e}')

# 解の計算と出力(2)
if d < 0: # d < 0
    x1d = (-b - d.sqrt()) / (2 * a)
else:
    x1d = (-b + d.sqrt()) / (2 * a)
x2d = c / (a * x1d)
print(f'x1d, x2d = {x1d:10.5e}, {x2d:10.5e}')

# 相対誤差
if abs(x1) > abs(x2):
    print('rE(x1) = ', abs(x1 - x1d) / abs(x1d))
    print('rE(x2) = ', abs(x2 - x2d) / abs(x2d))
else:
    print('rE(x1) = ', abs(x1 - x2d) / abs(x2d))
    print('rE(x2) = ', abs(x2 - x1d) / abs(x1d))

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------