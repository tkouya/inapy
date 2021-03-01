# spline.py: スプライン一次元補間
import numpy as np
import scipy.interpolate as scinp
from tktools import relerr  # 相対誤差


# 真の関数
def true_func(x):
    return np.exp(np.cos(x))


# 補間点設定
num_points = 11
min_x, max_x = -5.0, 5.0

# 補間点算出
x = np.linspace(min_x, max_x, num_points)
y = true_func(x)

# 補間多項式導出
interpoly_linear = scinp.interpolate.interp1d(x, y)  # linearがデフォルト
interpoly_cubic = scinp.CubicSpline(x, y)  # 3次スプライン

# 誤差導出
x_in_detail = np.linspace(min_x, max_x, num_points * 10)
y_in_detail = true_func(x_in_detail)

y_interpoly_linear = interpoly_linear(x_in_detail)
y_interpoly_cubic = interpoly_cubic(x_in_detail)

relerr_linear = relerr(y_interpoly_linear, y_in_detail)
relerr_cubic = relerr(y_interpoly_cubic, y_in_detail)

print('max relerr of linear interpoly: ', np.max(relerr_linear))
print('max_relerr of cubic interpoly : ', np.max(relerr_cubic))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
