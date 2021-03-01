# newton_cbrt.py: Newton法による立方根計算
import numpy as np


# Newton法による立方根計算
def newton_cbrt(x, rtol, atol):
    old_cbrt = float(x)
    new_cbrt = old_cbrt
    for times in range(0, 100):  # 最大100回
        new_cbrt = (2.0 * old_cbrt + x / old_cbrt ** 2) / 3.0
        if abs(new_cbrt - old_cbrt) <= abs(old_cbrt) * rtol + atol:
            return new_cbrt, times
        old_cbrt = new_cbrt

    return new_cbrt, times


# 収束条件
rel_tol = 1.0e-10
abs_tol = 1.0e-50

# x = 3
x = 3.0
true_val = np.cbrt(x)
newton_val, iter_times = newton_cbrt(x, rel_tol, abs_tol)
print('math.cbrt(', x, ') = ', true_val)
print('newton   (', x, ') = ', newton_val, ', Iter.Times = ', iter_times)
print('Relative Error     = ', np.fabs((true_val - newton_val) / true_val))

# x = 12345
x = 12345.0
true_val = np.cbrt(x)
newton_val, iter_times = newton_cbrt(x, rel_tol, abs_tol)
print('math.cbrt(', x, ') = ', true_val)
print('newton   (', x, ') = ', newton_val, ', Iter.Times = ', iter_times)
print('Relative Error     = ', np.fabs((true_val - newton_val) / true_val))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
