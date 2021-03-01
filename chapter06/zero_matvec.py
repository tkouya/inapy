# zero_matvec.py: 零ベクトル・零行列・単位行列など
import numpy as np

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim)  # 文字列→整数

# 零ベクトル
zero_vector = np.zeros(dim)

# 零行列
zero_matrix = np.zeros((dim, dim))

# 単位行列
unit_matrix = np.eye(dim)  # np.identity(dim)でも可

print('0 = ', zero_vector)
print('O = \n', zero_matrix)
print('I = \n', unit_matrix)

# 全ての成分が1のベクトルと行列
one_vector = np.ones(dim)
one_matrix = np.ones((dim, dim))

print('one_vector = ', one_vector)
print('one_matrix = \n', one_matrix)

# 乱数行列
rand_matrix = np.random.rand(dim, dim)
print('rand_matrix = \n', rand_matrix)


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
