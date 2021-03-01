# relerr.py: 問題3.5 誤差，有効桁数
import math

# 近似値
a_tilda = 141421

# 真値
a_true = 100000 * math.sqrt(2.0)

# 絶対誤差，相対誤差，有効桁数
abserr = math.fabs(a_true - a_tilda)
relerr = abserr
if a_true != 0.0:
    relerr /= math.fabs(a_true)
dec_digits = math.floor(-math.log10(relerr))
bin_digits = math.floor(-math.log(relerr) / math.log(2.0))  # 底の変換

print(f'  真値: {a_true:25.17e}')
print(f'近似値: {a_tilda:25.17e}')
print(f'絶対誤差: {abserr:10.3e}')
print(f'相対誤差: {relerr:10.3e}')
print(f'10進有効桁数: {dec_digits:10d}')
print(f' 2進有効桁数: {bin_digits:10d}')


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
