# complex_calc.py: 複素数型の計算
a = 1.2 + 3.4 * 1j # 1.2 + 3.4 i
b = complex(2.3, -4.5) # 2.3 - 4.5 i
print('a = ', a)
print('b = ', b)
print('i = ', 1j, ', i^2 = ', 1j ** 2)

# 四則演算
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)

import cmath # 複素関数
c = cmath.sqrt(a)
print('sqrt(a) = ', cmath.sqrt(a))
print('(sqrt(a)^2 = ', c ** 2)

# 指数関数，三角関数，対数関数
print('exp(a) = ', cmath.exp(a))
print('sin(a) = ', cmath.sin(a))
print('log(a) = ', cmath.log(a))
print('log10(a) = ', cmath.log10(a))
