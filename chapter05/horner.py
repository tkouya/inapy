# horner.py: Horner法
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

# x = sqrt(3)
x = np.sqrt(3.0)
print('horner p(', x, ') = ', horner_poly(x, poly_coef))
print('Numpy  p(', x, ') = ', p(x))
