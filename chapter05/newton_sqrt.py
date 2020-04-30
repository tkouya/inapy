# newton_sqrt.py: Newton法による平方根計算
# 平方根
import math

# Newton法による平方根計算
def newton_sqrt(x, rtol, atol):
	old_sqrt = float(x)
	new_sqrt = old_sqrt
	for times in range(0, 10): # 最大10回
		new_sqrt = (old_sqrt + x / old_sqrt) / 2.0
		if abs(new_sqrt - old_sqrt) <= abs(old_sqrt) * rtol + atol:
			return new_sqrt, times
		old_sqrt = new_sqrt

	return new_sqrt, times

# 収束条件
rel_tol = 1.0e-10
abs_tol = 0.0

# x = 3
x = 3.0
true_val = math.sqrt(x)
newton_val, iter_times = newton_sqrt(x, rel_tol, abs_tol)
print('math.sqrt(', x, ') = ', true_val)
print('newton   (', x, ') = ', newton_val, ', Iter.Times = ', iter_times)
print('Relative Error     = ', math.fabs((true_val - newton_val) / true_val))

# x = 12345
x = 12345.0
true_val = math.sqrt(x)
newton_val, iter_times = newton_sqrt(x, rel_tol, abs_tol)
print('math.sqrt(', x, ') = ', true_val)
print('newton   (', x, ') = ', newton_val, ', Iter.Times = ', iter_times)
print('Relative Error     = ', math.fabs((true_val - newton_val) / true_val))
