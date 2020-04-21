# cg_mpmath.py : 多倍長精度Conjugate-Gradient法
import mpmath # 多倍長精度計算
import numpy as np
# 時間計測
import time

# 計算精度設定
mpmath.mp.dps = 30
