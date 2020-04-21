# bench_matmul_mpmath.py: 多倍長精度行列乗算ベンチマークテスト
import math
import gmpy2

import numpy as np
import mpmath
import time

# Profile
import cProfile

# 計算桁数設定
for prec in [53, 106, 159, 212]:

	# mpmath backend
	print('mpmath.libmp.BACKEND = ', mpmath.libmp.BACKEND)
	mpmath.mp.prec = prec
	mp_sqrt2 = mpmath.mp.sqrt(mpmath.mp.mpf(2))
	mp_sqrt3 = mpmath.mp.sqrt(mpmath.mp.mpf(3))
	print('mpmath.prec = ', mpmath.mp.prec, 'mpmath.dps = ', mpmath.mp.dps)

	# gmpy2
	gmpy2.get_context().precision = prec # in bits
	print(gmpy2.get_context())
	#print(gmpy2.sqrt(gmpy2.mpfr(2)))

	mpfr_sqrt2 = gmpy2.sqrt(gmpy2.mpfr(2))
	mpfr_sqrt3 = gmpy2.sqrt(gmpy2.mpfr(3))
	#print('a = ', a)
	print('mpfr_sqrt2 = ', mpfr_sqrt2)
	print('mpfr_sqrt3 = ', mpfr_sqrt3)

	# Frobenius norm
	def xd_norm_fro(mat, row_dim, col_dim, xd_zero):
		ret = xd_zero

		for i in range(0, row_dim):
			for j in range(0, col_dim):
				ij_index = i * col_dim + j
				ret += mat[ij_index] ** 2
		ret = ret ** (0.5)

		return ret

	# 自作行列乗算
	def xd_mymatmul(mat_a, row_dim_mat_a, col_dim_mat_a, mat_b, row_dim_mat_b, col_dim_mat_b, xd_zero):
		row_dim  , mid_dim = row_dim_mat_a, col_dim_mat_a
		mid_dim_b, col_dim = row_dim_mat_b, col_dim_mat_b
	#   print('row_dim, mid_dim, col_dim = ', row_dim, mid_dim, col_dim)

		zero = xd_zero

		if mid_dim != mid_dim_b:
			print('A\'s col_dim = ', mid_dim, ', B\'s row_dim = ', mid_dim_b, ' are mismatched!.')
			return [zero]

		mat_c = [zero] * (row_dim * col_dim)

		for i in range(0, row_dim):
			for j in range(0, col_dim):
				ij_index = i * col_dim + j
				mat_c[ij_index] = zero
				for k in range(0, mid_dim):
					ik_index = i * mid_dim + k
					kj_index = k * mid_dim + j
					mat_c[ij_index] += mat_a[ik_index] * mat_b[kj_index]

		return mat_c

	# 自作行列乗算
	for sq_dim in [32, 64, 128, 256]:

		# float

		# dimension
		row_dim = sq_dim
		mid_dim = sq_dim
		col_dim = sq_dim
		d_zero  = 0.0
		mp_zero = mpmath.mp.mpf(0)
		mpfr_zero = gmpy2.mpfr(0)

		# A := sqrt(2) * [(i + j + 1)]
		d_mat_a  = [ d_zero] * (row_dim * mid_dim)
		mp_mat_a = [mp_zero] * (row_dim * mid_dim)
		mpfr_mat_a = [mpfr_zero] * (row_dim * mid_dim)
		mpmat_a = mpmath.matrix(row_dim, mid_dim) # matirx type in mpmath

	#	print('size_mat_a = ', len(dd_mat_a))
		for i in range(row_dim):
			for j in range(mid_dim):
				ij_index = i * mid_dim + j
				d_mat_a [ij_index] = float(mpfr_sqrt2 * (i + j + 1))
				mp_mat_a[ij_index] = mp_sqrt2 * mpmath.mp.mpf(i + j + 1)
				mpfr_mat_a[ij_index] = mpfr_sqrt2 * gmpy2.mpfr(i + j + 1)
				mpmat_a[i, j] = mp_mat_a[ij_index]

		# B := sqrt(3) * [max(i + 1, j + 1)]
		d_mat_b  = [ d_zero] * (mid_dim * col_dim)
		mp_mat_b = [mp_zero] * (mid_dim * col_dim)
		mpfr_mat_b = [mpfr_zero] * (mid_dim * col_dim)
		mpmat_b = mpmath.matrix(mid_dim, col_dim)

	#	print('size_mat_b = ', len(dd_mat_b))
		for i in range(mid_dim):
			for j in range(col_dim):
				ij_index = i * col_dim + j
				if i > j:
					d_mat_b[ij_index]  = float(mpfr_sqrt3 * (i + 1))
					mp_mat_b[ij_index] = mp_sqrt3 * mpmath.mp.mpf(i + 1)
					mpfr_mat_b[ij_index] = mpfr_sqrt3 * gmpy2.mpfr(i + 1)
				else:
					d_mat_b[ij_index]  = float(mpfr_sqrt3 * (j + 1))
					mp_mat_b[ij_index] = mp_sqrt3 * mpmath.mp.mpf(j + 1)
					mpfr_mat_b[ij_index] = mpfr_sqrt3 * gmpy2.mpfr(j + 1)

				mpmat_b[i, j] = mp_mat_b[ij_index]

		print('double= ', xd_norm_fro(d_mat_a, row_dim, mid_dim, d_zero) , xd_norm_fro(d_mat_b, mid_dim, col_dim, d_zero))
		print('mp    = ', xd_norm_fro(mp_mat_a, row_dim, mid_dim, mp_zero), xd_norm_fro(mp_mat_b, mid_dim, col_dim, mp_zero))
		print('mpmat = ', mpmath.mnorm(mpmat_a, 'f'), mpmath.mnorm(mpmat_b, 'f'))
		print('mpfr  = ', xd_norm_fro(mpfr_mat_a, row_dim, mid_dim, mpfr_zero), xd_norm_fro(mpfr_mat_b, mid_dim, col_dim, mpfr_zero))

		# double
		start_time = time.time()
		d_mat_c = xd_mymatmul(d_mat_a, row_dim, mid_dim, d_mat_b, mid_dim, col_dim, d_zero)
		end_time = time.time()
		d_matmul_time = end_time - start_time
		print('d(', 53, ')')
		#cProfile.run('xd_mymatmul(d_mat_a, row_dim, mid_dim, d_mat_b, mid_dim, col_dim, d_zero)')

		# mpmath
		start_time = time.time()
		mp_mat_c = xd_mymatmul(mp_mat_a, row_dim, mid_dim, mp_mat_b, mid_dim, col_dim, mp_zero)
		end_time = time.time()
		mp_matmul_time = end_time - start_time
		print('mp(', mpmath.mp.prec, ')')
		#cProfile.run('xd_mymatmul(mp_mat_a, row_dim, mid_dim, mp_mat_b, mid_dim, col_dim, mp_zero)')
	#	print('sq_dim = ', sq_dim, ' qd_mymatmul 計算時間(秒): ', end_time - start_time)

		# matrix in mpmath
		start_time = time.time()
		mpmat_c = mpmat_a * mpmat_b
		end_time = time.time()
		mpmatmul_time = end_time - start_time
		print('mp(', mpmath.mp.prec, ')')
		#cProfile.run('mpmat_c = mpmat_a * mpmat_b')
	#	print('sq_dim = ', sq_dim, ' qd_mymatmul 計算時間(秒): ', end_time - start_time)

		# mpfr
		start_time = time.time()
		mpfr_mat_c = xd_mymatmul(mpfr_mat_a, row_dim, mid_dim, mpfr_mat_b, mid_dim, col_dim, mpfr_zero)
		end_time = time.time()
		mpfr_matmul_time = end_time - start_time
		print('mpfr(', gmpy2.get_context().precision, ')')
		#cProfile.run('xd_mymatmul(mpfr_mat_a, row_dim, mid_dim, mpfr_mat_b, mid_dim, col_dim, mpfr_zero)')
	#	print('sq_dim = ', sq_dim, ' qd_mymatmul 計算時間(秒): ', end_time - start_time)

		print('sq_dim = ', sq_dim, f', d, mp({mpmath.mp.prec:5d}), mpmat({mpmath.mp.prec:5d}), mpfr({gmpy2.get_context().precision:5d}): {d_matmul_time:5.3f}, {mp_matmul_time:5.3f}, {mpmatmul_time:5.3f}, {mpfr_matmul_time:5.3f}')

		print('double= ', xd_norm_fro(d_mat_c, row_dim, col_dim, d_zero))
		print('mp    = ', xd_norm_fro(mp_mat_c, row_dim, col_dim, mp_zero))
		print('mpmat = ', mpmath.mnorm(mpmat_c, 'f'))
		print('mpfr  = ', xd_norm_fro(mpfr_mat_c, row_dim, col_dim, mpfr_zero))

		# delete
		del d_mat_a, d_mat_b, d_mat_c
		del mp_mat_a, mp_mat_b, mp_mat_c
		del mpmat_a, mpmat_b, mpmat_c
		del mpfr_mat_a, mpfr_mat_b, mpfr_mat_c
