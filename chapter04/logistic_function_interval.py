# logistic_function_interval.py: ロジスティック写像
from interval import Interval  # 区間演算ライブラリ

x = [Interval(0.7501)]  # 初期値を配列の先頭値に格納

# x[i+1]に値を追加
const4 = Interval(float(4))  # const4 := 4
const1 = Interval(float(1))  # const1 := 1
for i in range(0, 100):
    x.append(const4 * x[i] * (const1 - x[i]))

# x[0], x[10], ..., x[100]を表示
print('    i, [       x[i].left         ,         x[i].right       ]')
for i in range(0, 101):
    if i % 10 == 0:
        print(f'{i:5d}, [{x[i].left:25.17e}, {x[i].right:25.17e}]')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
