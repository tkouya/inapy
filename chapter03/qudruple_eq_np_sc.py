# quadruple_eq_np_sc.py: 2次方程式
import numpy as np
import scipy as sc

# 係数
# p(x) = 2 * x^2 + 6 * x + 4
# p = np.poly1d([2, 6, 4])
# p(x) = 2 * x^2 + 3 * x + 4
p = np.poly1d([2, 3, 4])

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
d = p.coef[1] ** 2 - 4 * p.coef[0] * p.coef[2]
np_ans = [(-p.coef[1] + np.sqrt(d)) / (2 * p.coef[0]), (-p.coef[1] - np.sqrt(d)) / (2 * p.coef[0])]
sc_ans = [(-p.coef[1] + sc.sqrt(d)) / (2 * p.coef[0]), (-p.coef[1] - sc.sqrt(d)) / (2 * p.coef[0])]
print('解の公式(np_ans): ', np_ans)
print('検算: ', np.polyval(p, np_ans))
print('解の公式(sc_ans): ', sc_ans)
print('検算: ', np.polyval(p, np_ans))
