# logistic_function_mpmath.py : ロジスティック写像(mpmath版)
import mpmath

print('mpmath.libmp.BACKEND = ', mpmath.libmp.BACKEND)

# 10進40桁計算
mpmath.mp.dps = 40  # 仮数部の10進桁数(P.49では350桁指定)
x = [mpmath.mp.mpf('0.7501')]
for i in range(0, 100):
    x.append(4 * x[i] * (1 - x[i]))

# 10進80桁計算
mpmath.mp.dps = 80  # P.49では500桁指定
xl = [mpmath.mp.mpf('0.7501')]
for i in range(0, 100):
    xl.append(4 * xl[i] * (1 - xl[i]))

reldiff_x = [mpmath.fabs((xl[i] - x[i]) / xl[i]) for i in range(len(x))]

print('    i,                      x[i]                   , reldiff_x[i]')
for i in range(0, 101):
    if i % 10 == 0:
        print(
            f'{i:5d}, ',
            mpmath.nstr(x[i], 40),
            ', ',
            mpmath.nstr(reldiff_x[i], 2)
        )


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
