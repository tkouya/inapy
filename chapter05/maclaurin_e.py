# maclaurin_e.py: Maclaurin展開に基づくeの計算
# math
import math

# Maclaurin展開に基づくexp(x)
def maclaurin_e(m):
	old_ret = 1.0
	ret = old_ret
	coef = 1.0 # coef := 0! = 1
	for i in range(1, m):
		coef /= i # coef := 1/i!
		ret = old_ret + coef
		old_ret = ret

	return ret


# 項数mとhat(e_m)
print('  m           hat(e_m)           ')
for m in range(1, 10):
    print(f'{m:3d} {maclaurin_e(m):25.17e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
