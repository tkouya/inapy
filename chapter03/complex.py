# 複素数の扱い方
import math #

a = complex(3, 2)
print("a = ", a) # a == 3 + 2 * j

print("Re(a) = ", a.real)
print("Im(a) = ", a.imag)

print("a = (r, theta) = ", abs(a), math.atan2(a.real, a.imag))
