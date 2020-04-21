# newton_sqrt.py: Newton法による平方根計算
# random
import random
# 平方根
import math

# Newton法による平方根計算
def newton_sqrt(x, rtol, atol):
	old_sqrt = float(x)
	new_sqrt = old_sqrt
	for times in range(0, 10): # 最大10回
		new_sqrt = (old_sqrt + x / old_sqrt) / 2.0
		if abs(new_sqrt - old_sqrt) <= abs(old_sqrt) * rtol + atol:
			return new_sqrt
		old_sqrt = new_sqrt

	return ret, times

# x = random
rtol = 1.0e-10
atol = 0.0
print(f'     x    ,newton_sqrt(x,{rtol:5.1g},{atol:5.1g}),         math.sqrt(x)     ,   reldiff  ')
for times in range(0, 10):
	x = random.uniform(0, 1000) # [0, 100]の任意小数
	newton_val = newton_sqrt(x, rtol, atol) # 手製Newton法
	math_val = math.sqrt(x) # math.sqrt
	reldiff = math.fabs(math_val)
	if reldiff != 0.0:	reldiff = math.fabs(newton_val - math_val) / reldiff
	print(f'{x:10.3e}, {newton_val:25.17e}, {math_val:25.17e}, {reldiff:10.3e}')
