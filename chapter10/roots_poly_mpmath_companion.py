# roots_poly_mpmath.py : 多倍長計算で代数方程式を解く
import numpy as np
import mpmath

# coef := mp_poly1d(list)
def mp_poly1d(list):
	len_list = len(list)
	deg = len_list - 1
	for i in range(len_list):
		tmp_mpf = mpmath.mpf(str(list[i]))
		if(tmp_mpf != mpmath.mpf('0.0')):
			break
		deg -= 1

	coef = [mpmath.mpf('0.0')] * (deg + 1)
#	print('len, deg = ', len_list, deg)
	for i in range(deg + 1):
		coef[deg - i] = mpmath.mpf(str(list[len_list - i - 1]))

	return coef

# ret := mp_poly_a * mp_poly_b
def mp_poly1d_mul(mp_poly_a, mp_poly_b):
	len_mp_poly_a = len(mp_poly_a)
	len_mp_poly_b = len(mp_poly_b)
	len_mp_poly_ret = len_mp_poly_a + len_mp_poly_b - 1

	mp_poly_ret = [mpmath.mpf('0.0')] * len_mp_poly_ret

	for i in range(len_mp_poly_a):
		for j in range(len_mp_poly_b):
			mp_poly_ret[i + j] += mp_poly_a[i] * mp_poly_b[j]

	return mp_poly_ret

# ret := (x - roots[0]) * ... * (x - roots[n - 1])
def mp_roots2poly1d(mp_roots):
	mp_poly_ret = mp_poly1d([1])
	for i in range(len(mp_roots)):
		mp_poly_ret = mp_poly1d_mul(mp_poly_ret, mp_poly1d([1, -mp_roots[i]]))

	return mp_poly_ret

# 次数
max_deg = 20

# 真の解 : true_roots = [n, n-1, ..., 1]
true_roots = np.array(range(max_deg, 0, -1))
print('true_roots = ', true_roots)

# 多項式p(x) = (x - n) * ... * (x - 1) の係数を生成
poly_coef = np.poly(true_roots)
print('polynomial = ', poly_coef)

# 代数方程式の解(根)を導出
approx_roots = np.roots(poly_coef)
print('approx_roots = ', approx_roots)
relerr_approx_roots = np.abs((approx_roots - true_roots) / true_roots)
print('relerr       = ', relerr_approx_roots)

# 多倍長浮動小数点化
mpmath.mp.dps = 200  # 10進200桁
mpmath.mp.trap_complex = True
print(mpmath.mp)

# mpmath.polyroots使用 → 失敗
mp_true_roots = [mpmath.mpf(str(i)) for i in range(max_deg, 0, -1)]
print('mp_true_roots = ', mp_true_roots)

mp_poly_coef = mp_roots2poly1d(mp_true_roots)

# Companion行列生成
dim = len(mp_poly_coef) - 1
mp_companion_mat = mpmath.matrix(dim, dim)
for i in range(dim - 1):
	mp_companion_mat[i, i + 1] = mpmath.mpf('1')
for i in range(dim):
	mp_companion_mat[dim - 1, i] = -mp_poly_coef[dim - i]

#print('companion_mat = ', mp_companion_mat)
mp_eig, mp_eig_error = mpmath.eig(mp_companion_mat)
mp_eig = mpmath.eig_sort(mp_eig, f = lambda x: -mpmath.re(x)) # 実部の絶対値の逆順にソート
mp_roots = [mpmath.re(mp_eig[i]) for i in range(len(mp_eig))]
print('eig           = '); mpmath.nprint(mp_roots)
mp_relerr_roots = [mpmath.fabs((mp_roots[i] - mp_true_roots[i]) / mp_true_roots[i]) for i in range(len(mp_roots))]
print('relerr        = '); mpmath.nprint(mp_relerr_roots)
