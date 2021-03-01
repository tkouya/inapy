# logistic_function_rmode.py: ロジスティック写像(丸め誤差評価付き)
import rmode  # 丸めモード変更

# デフォルトモード(RN)
rmode.print_rmode()
x_rn = [0.7501]  # 初期値を配列の先頭値に格納

# x[i+1]に値を追加
for i in range(0, 100):
    x_rn.append(4 * x_rn[i] * (1 - x_rn[i]))

# RPモード
rmode.set_rmode(rmode.FE_UPWARD)
rmode.print_rmode()
x_rp = [0.7501]  # 初期値を配列の先頭値に格納

# x[i+1]に値を追加
for i in range(0, 100):
    x_rp.append(4 * x_rp[i] * (1 - x_rp[i]))

# RMモード
rmode.set_rmode(rmode.FE_DOWNWARD)
rmode.print_rmode()
x_rm = [0.7501]  # 初期値を配列の先頭値に格納

# x[i+1]に値を追加
for i in range(0, 100):
    x_rm.append(4 * x_rm[i] * (1 - x_rm[i]))

# diff_rn_rm, diff_rn_rp, diff_rp_rm
rel_diff_rn_rm = [abs((x_rn[i] - x_rm[i]) / x_rn[i]) for i in range(len(x_rn))]
rel_diff_rn_rp = [abs((x_rn[i] - x_rp[i]) / x_rn[i]) for i in range(len(x_rn))]
rel_diff_rm_rp = [abs((x_rm[i] - x_rp[i]) / x_rn[i]) for i in range(len(x_rn))]
max_rel_diff = [
    max(
        rel_diff_rn_rm[i],
        rel_diff_rn_rp[i],
        rel_diff_rm_rp[i]
    ) for i in range(len(x_rn))
]

# x[0], x[10], ..., x[100]を表示
print('    i,           x_rm[i]        ,           x_rn[i]        ,           x_rp[i]        ,max_rel_diff')
for i in range(0, 101):
    if i % 10 == 0:
        print(f'{i:5d}, {x_rm[i]:25.17e}, {x_rn[i]:25.17e}, {x_rp[i]:25.17e}, {max_rel_diff[i]:5.1e}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
