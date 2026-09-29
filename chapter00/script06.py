# script06.py: 6番目のPythonスクリプト
# util.は不要
from util import tkRational

# 有理数(分数)クラス
a = tkRational(5, 3)
print('a = ', a)
b = tkRational(-3, 2)
print('b = ', b)

# 加算
c = a + b
print('a + b = c -> ', c)

# 減算，乗算，除算
print('a - b = c -> ', a - b)
print('a * b = c -> ', a * b)
print('a / b = c -> ', a / b)

# 演習問題3
c = tkRational(324, 25) - tkRational(24, 55)
d = (tkRational(3, 2) + tkRational(5, 12)) / tkRational(25, 33)
print('c = ', c)
print('d = ', d)

# -------------------------------------
# Copyright (c) 2026 Tomonori Kouya
# All rights reserved.
# -------------------------------------
