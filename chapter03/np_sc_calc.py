# np_sc_calc.py: NumPyとSciPy
import numpy as np # NumPy
import scipy as sc # SciPy

# a = 3.0 
a = -3.0
z = -1.0 + 2.0 * 1j
#z = np.complex(-1.0, 2.0)

print('a = ', a)
print('z = ', z)

# 平方根: NumPy
print('np.sqrt(a) = ', np.sqrt(a))
print('np.sqrt(z) = ', np.sqrt(z))

# 平方根: SciPy
print('sc.sqrt(a) = ', sc.sqrt(a))
print('sc.sqrt(z) = ', sc.sqrt(z))

# べき乗: NumPy
c = np.sqrt(a); w = np.sqrt(z)
print('(np.sqrt(a))^2 = ', c ** 2)
print('(np.sqrt(z))^2 = ', w ** 2)

# べき乗: SciPy
c = sc.sqrt(a); w = sc.sqrt(z)
print('(sc.sqrt(a))^2 = ', c ** 2)
print('(sc.sqrt(z))^2 = ', w ** 2)

# 指数関数，三角関数，対数関数: NumPy
print('np.exp(a)   = ', np.exp(a))
print('np.sin(a)   = ', np.sin(a))
print('np.log(a)   = ', np.log(a))
print('np.log10(a) = ', np.log10(a))
print('np.exp(z)   = ', np.exp(z))
print('np.sin(z)   = ', np.sin(z))
print('np.log(z)   = ', np.log(z))
print('np.log10(z) = ', np.log10(z))

# 指数関数，三角関数，対数関数: SciPy
print('sc.exp(a)   = ', sc.exp(a))
print('sc.sin(a)   = ', sc.sin(a))
print('sc.log(a)   = ', sc.log(a))
print('sc.log10(a) = ', sc.log10(a))
print('sc.exp(z)   = ', sc.exp(z))
print('sc.sin(z)   = ', sc.sin(z))
print('sc.log(z)   = ', sc.log(z))
print('sc.log10(z) = ', sc.log10(z))
