# horner.py: Horner法
# random
import random
# numpy多項式と比較
from numpy import poly1d as nppoly
# nump
import numpy as np

# Horner法
def horner_poly(x, coef):
	deg = len(coef) # deg = 次数 - 1
	ret = coef[0]
	for i in range(0, deg - 1):
		ret = ret * x + coef[i + 1]

	return ret

# p(x) = (-4) * x^3 + 3 * x^2 + (-2) * x + 1
poly_coef = [-4.0, 3.0, -2.0, 1.0]
print('poly_coef = ', poly_coef)

# numpy.poly1d
p = nppoly(poly_coef)
print('p(x) = \n', p)

# x = random
print('     x    ,       horner_poly(x)     ,        numpy.poly1(x)    ,   reldiff  ')
for times in range(0, 10):
	x = random.uniform(-100, 100) # [-100, 100]の任意小数
	horner_val = horner_poly(x, poly_coef) # 手製Horner法
	numpy_val = p(x) # numpy.poly1d
	reldiff = np.abs(numpy_val)
	if(reldiff != 0.0):	reldiff = np.abs(horner_val - numpy_val) / reldiff
	print(f'{x:10.3e}, {horner_val:25.17e}, {numpy_val:25.17e}, {reldiff:10.3e}')
