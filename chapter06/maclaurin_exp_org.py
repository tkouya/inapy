# maclaurin_exp.py: Maclaurin展開に基づく初等関数計算
# math
import math
# linspace
import numpy as np

# Maclaurin展開に基づくexp(x)
def maclaurin_exp(x, rtol, atol, max_deg):
	old_ret = 1.0
	ret = old_ret
	xn = 1.0
	coef = 1.0 # 1/0!
	for i in range(1, max_deg):
		coef /= i # coef = 1/i!
		xn *= x   # xn = x^n
		ret = old_ret + coef * xn
		if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
			return ret
		old_ret = ret

	return ret

# Maclaurin展開に基づくexp(x) : reduction
def maclaurin_exp_m1(x, rtol, atol, max_deg):
	org_x = x
	x = math.fabs(x)
	int_x = math.floor(x)
	x = x - int_x

	old_ret = 1.0
	ret = old_ret
	xn = 1.0
	coef = 1.0 # 1/0!
	for i in range(1, max_deg):
		coef /= i # coef = 1/i!
		xn *= x   # xn = x^n
		ret = old_ret + coef * xn
		if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
			break;
		old_ret = ret

	# * exp(int_x)
	ret *= math.e ** int_x

	# x < 0
	if org_x < 0:
		ret = 1 / ret

	return ret

# x = random
rtol = 1.0e-10
atol = 0.0
max_deg = 100
x_array = np.linspace(-100, 100, num = 20) # [-100, 100]
print('     x    ,     maclaurin_exp(x)     ,        math.exp(x)       ,   reldiff  ')
for x in x_array:
#	maclaurin_val = maclaurin_exp(x, rtol, atol, max_deg) # 手製exp関数
	maclaurin_val = maclaurin_exp_m1(x, rtol, atol, max_deg) # 手製exp関数
	math_val = math.exp(x) # math.exp
	reldiff = math.fabs(math_val)
	if reldiff != 0.0: reldiff = math.fabs(maclaurin_val - math_val) / reldiff
	print(f'{x:10.3e}, {maclaurin_val:25.17e}, {math_val:25.17e}, {reldiff:10.3e}')
