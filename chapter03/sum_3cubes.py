# sum_3cube.py: 立方の和
#
# a = 4
# b = 4
# c = -5
# [int  ] a^3 + b^3 + c^3 =  3
# [float] a^3 + b^3 + c^3 =  3.0

# a = 37404275617
# b = -25282289375
# c = -33071554596
# [int  ] a^3 + b^3 + c^3 =  2
# [float] a^3 + b^3 + c^3 =  0.0

a = input('a = ')
b = input('b = ')
c = input('c = ')

# 整数に変換
ia = int(a)
ib = int(b)
ic = int(c)
444
print('[int  ] a^3 + b^3 + c^3 = ', ia**3 + ib**3 + ic**3)

# 浮動小数点数に変換
fa = float(a)
fb = float(b)
fc = float(c)

print('[float] a^3 + b^3 + c^3 = ', fa**3 + fb**3 + fc**3)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
