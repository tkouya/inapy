# logistic_function_mpmath.py : ロジスティック写像(多倍長浮動小数点演算)
import mpmath

print('mpmath.libmp.BACKEND = ', mpmath.libmp.BACKEND)

# 10進40桁計算
mpmath.mp.dps = 40 # 仮数部の10進桁数
x = [mpmath.mp.mpf('0.7501')]
for i in range(0, 100):
	x.append(4 * x[i] * (1 - x[i]))

# 10進80桁計算
mpmath.mp.dps = 80
xl = [mpmath.mp.mpf('0.7501')]
for i in range(0, 100):
	xl.append(4 * xl[i] * (1 - xl[i]))

reldiff_x = [mpmath.fabs((xl[i] - x[i]) / xl[i]) for i in range(len(x))]

print('    i,                      x[i]                   , reldiff_x[i]')
for i in range(0, 101):
	if i % 10 == 0:
		print(f'{i:5d}, ', mpmath.nstr(x[i], 40), ', ', mpmath.nstr(reldiff_x[i], 2))
