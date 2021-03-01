# test_decimal.py: 10進浮動小数点演算例
import decimal as dec  # 10進多倍長精度演算

# 計算コンテキスト確認
print('current decimal context = ', dec.getcontext())

# 10進5桁計算
dec.getcontext().prec = 5
# 四捨五入
dec.getcontext().rounding = dec.ROUND_HALF_UP

# 計算コンテキスト確認
print('current decimal context = ', dec.getcontext())

# 演習問題1
a = dec.Decimal('2.3456e+2')
b = dec.Decimal('3.1415')

print(f'a + b = {a + b:10.4e}')
print(f'a - b = {a - b:10.4e}')
print(f'a * b = {a * b:10.4e}')
print(f'a / b = {a / b:10.4e}')

# 演習問題2
sqrt2 = dec.Decimal('2.0000').sqrt()
int3 = dec.Decimal('3.0000')
div32 = dec.Decimal('2.0000') / dec.Decimal('3.0000')
print(f'sqrt(2) = {sqrt2:10.4e}')
print(f'      3 = {int3:10.4e}')
print(f'  2 / 3 = {div32:10.4e}')

print(f'      x = {(int3 + div32) / sqrt2:10.4e}')

# 演習問題5
shaku1 = dec.Decimal('10.000') / dec.Decimal('33.000')
ken1 = dec.Decimal('6.0000') * shaku1
tsubo1 = ken1 * ken1
print(f'1 Tsubo = {tsubo1:10.4e} m^2')

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
