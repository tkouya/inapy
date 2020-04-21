# 2次方程式
import numpy as np
import scipy as spy

# 係数
# p(x) = 2 * x^2 + 3 * x + 4
#p = np.poly1d([2, 3, 4])
# p(x) = x^2 + 3 * x - 4
#p = np.poly1d([1, 3, -4])
# p(x) = 1.01 * x^2 +2718281 * x + 0.01
p = np.poly1d([1.01, 2718281, 0.01])
# p(x) = 3 * x^2 -350 * x + 2
#p = np.poly1d([3, -350, 2])

# 確認
print(p)

# p(x)の係数
print('係数 [a, b, c] = ', p.coef)
print('a = p.coef[0] = ', p.coef[0])
print('b = p.coef[1] = ', p.coef[1])
print('c = p.coef[2] = ', p.coef[2])

# p(x) = 0の解
print('解(roots): ', p.roots)

# 検算: p(r) == 0?
print('検算: ', np.polyval(p, p.roots))

# 解の公式(1)
d = p.coef[1]**2 - 4 * p.coef[0] * p.coef[2]
#ans = [(-p.coef[1] + np.sqrt(d)) / (2 * p.coef[0]), (-p.coef[1] - np.sqrt(d)) / (2 * p.coef[0])]
ans = [(-p.coef[1] + spy.sqrt(d)) / (2 * p.coef[0]), (-p.coef[1] - spy.sqrt(d)) / (2 * p.coef[0])]
print('解の公式: ', ans)
print('検算: ', np.polyval(p, ans))
# 解の公式(2)
d = p.coef[1]**2 - 4 * p.coef[0] * p.coef[2]
#ans = [(-p.coef[1] + np.sqrt(d)) / (2 * p.coef[0]), (-p.coef[1] - np.sqrt(d)) / (2 * p.coef[0])]
ans = [(-p.coef[1] - spy.sign(p.coef[1]) * spy.sqrt(d)) / (2 * p.coef[0]), 0]
ans[1] = p.coef[2] / (p.coef[0] * ans[0])
print('解の公式: ', ans)
print('検算: ', np.polyval(p, ans))
