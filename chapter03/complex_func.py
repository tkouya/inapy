# complex_func.py: 複素関数の計算
import cmath # 複素関数

a = 1.2 + 3.4j # 1.2 + 3.4 i
print('a = ', a)

c = cmath.sqrt(a)
print('sqrt(a) = ', cmath.sqrt(a))
print('sqrt(a)^2 = ', c ** 2)

# 指数関数，三角関数，対数関数
print('exp(a) = ', cmath.exp(a))
print('sin(a) = ', cmath.sin(a))
print('log(a) = ', cmath.log(a))
print('log10(a) = ', cmath.log10(a))

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
