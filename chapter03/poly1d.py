# 多項式関数
from numpy import poly1d as poly

# p(x) = 2 * x^2 + 3 * x + 4
p = poly([2, 3, 4])

# 確認
print(p)

# q(x) = -x^2 - 20*x + 20
q = poly([-1, -20, 20])

# 確認
print(q)

# x in [-10, 10]
import numpy as np

x = np.linspace(-10, 10, num = 50) # 50点
y_p = p(x)
y_q = q(x)

# 確認
print('x = ', x)
print('y_p = ', y_p)
print('y_q = ', y_q)

# p(x)とq(x)の交点を求める。
r = p - q
print("Solve p - q = 0 -> ", r.r)

# 検算
print("r(x) = 0 ? ->", r(r.r)) 

# グラフを描画
import matplotlib.pyplot as plot

figure, axis = plot.subplots()
axis.plot(x, y_p)
axis.plot(x, y_q)
axis.set(xlabel = 'x', ylabel= 'y', title = 'p(x), q(x)')
axis.grid()
figure.savefig('poly1d.svg')
plot.show()



