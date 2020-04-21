# 
import mpmath
import numpy as np

# 多倍長精度設定
mpmath.mp.dps = 30

print('np.pi = ', np.pi)
print('mp.pi = ', mpmath.mp.pi)
