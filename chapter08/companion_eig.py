# companion_eig.py : コンパニオン行列
import numpy as np
import scipy.linalg as slinalg

# Companion行列と固有値
# p(x) = 4 * x^3 + 3 * x^2 + 2 * x + 1 = 0
poly_coef = [4, 3, 2, 1]
mat_c = slinalg.companion(poly_coef)
print('Companion matrix = \n', mat_c)
eigval, ev = slinalg.eig(mat_c)
ev = ev.T
print('Eigenvalues = ', eigval)
print('Eigenvectors = ', ev)
# C * v = lambda * v ?
for i in range(0, eigval.size) :
	print('|| C * v - lambda[', i, '] * v||_2 = ', slinalg.norm(mat_c @ ev[i].T - eigval[i] * ev[i]))

# p(lambda) = 0?
eigpoly = np.poly1d(poly_coef)
for i in range(eigval.size) :
	print('p(lambda[', i, ']) = ', eigpoly(eigval[i]))

