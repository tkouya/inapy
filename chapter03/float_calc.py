# float_calc.py: 実数型の計算
a = input('a = ')
b = input('b = ')
a, b = float(a), float(b)

# 四則演算
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)

# 平方根: math.sqrt
import math # 数学関数
print('sqrt(a) = ', math.sqrt(a))

# べき乗
c = math.sqrt(b)
print('(sqrt(b))^2 = ', c ** 2)

# 指数関数，三角関数，対数関数
print('exp(a) = ', math.exp(a))
print('sin(a) = ', math.sin(a))
print('log(a) = ', math.log(a))
print('log10(a) = ', math.log10(a))
