# input_print.py: inputとprint

# aをキーボードから入力
a = input('a = ')
print('a = ', a, ', type(a) = ', type(a))

# bをキーボードから入力
b = input('b = ')

# a + bを計算
print('a + b = ', a + b)

# aとbを強制的にfloat型に変換
a, b = float(a), float(b)

# a + bを浮動小数点演算
print('a + b = ', a + b)

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
