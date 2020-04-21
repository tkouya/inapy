# Diophantine Problem: x^3 + y^3 + z^3 = n
import mpmath

#mpmath.mp.dps = 20 # Incorrect!
#mpmath.mp.dps = 30 # Incorrect!
#mpmath.mp.dps = 40 # Incorrect!
#mpmath.mp.dps = 45 # Incorrect!
#mpmath.mp.dps = 47 # Incorrect!
#mpmath.mp.dps = 48 # Incorrect!
#mpmath.mp.dps = 49 # Incorrect!
#mpmath.mp.dps = 50 # O.K.!
#mpmath.mp.dps = 100 # O.K.!

for dec_digits in range(40, 61):

	mpmath.mp.dps = dec_digits

	# 整数を入力
	x = mpmath.mp.mpf('-80538738812075974')
	y = mpmath.mp.mpf('80435758145817515')
	z = mpmath.mp.mpf('12602123297335631')

	n = x ** 3 + y ** 3 + z ** 3

	print('dec.digits = ', mpmath.mp.dps, ', ', x , '^3 + ', y, '^3 + ', z, '^3 = ', n)

