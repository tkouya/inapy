# logistic_function_gmpy2.py: ロジスティック写像(gmpy2版)
import gmpy2

# 128 bits
gmpy2.get_context().precision = 128
x = [gmpy2.mpfr('0.7501')]
for i in range(0, 100):
    x.append(4 * x[i] * (1 - x[i]))

# 256 bits
gmpy2.get_context().precision = 256
xl = [gmpy2.mpfr('0.7501')]
for i in range(0, 100):
    xl.append(4 * xl[i] * (1 - xl[i]))

reldiff_x = [gmpy2.reldiff(xl[i], x[i]) for i in range(len(x))]

print('    i,                          x[i]                          ')
for i in range(0, 101):
    if i % 10 == 0:
        print(f'{i:5d}, {x[i]:50.40e}, {reldiff_x[i]:5.1e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
