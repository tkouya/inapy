# print_format.py: 型指定出力
a = 10.65387

# 変数埋め込み書式指定
print(f'a = {a:25.17e}')
print(f'a = {a:+15.3f}')
print(f'a = {a:25.17g}')

# format関数使用
print('a = {:25.17e}'.format(a))

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
