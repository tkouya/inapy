# 基本線型計算ベンチマーク
import numpy as np
import scipy as spy

# 時間計測用
import time

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# 正方行列生成: 乱数行列
np.random.seed(20190326)
matrix_a = spy.random.rand(dim, dim)
matrix_b = spy.random.rand(dim, dim)

# 内容チェック
#print('A = ', matrix_a)
#print('B = ', matrix_b)

# 行列乗算(1): C1 = A * B
start_time = time.time()
matrix_c1 = matrix_a @ matrix_b
end_time = time.time()
print('C1 計算時間(秒): ', end_time - start_time)

# 行列乗算(2): C2 = A * B
start_time = time.time()
matrix_c2 = matrix_a.dot(matrix_b)
end_time = time.time()
print('C2 計算時間(秒): ', end_time - start_time)

# 検算: ||C1 - C2|| == 0?
print('||C1 - C2|| = ', np.linalg.norm(matrix_c1 - matrix_c2))

# 複素正方行列生成: 乱数行列
cmatrix_a = spy.random.rand(dim, dim) + 1j * spy.random.rand(dim, dim)
cmatrix_b = spy.random.rand(dim, dim) + 1j * spy.random.rand(dim, dim)

# 行列乗算(1): C1 = A * B
start_time = time.time()
cmatrix_c1 = cmatrix_a @ cmatrix_b
end_time = time.time()
print('CC1 計算時間(秒): ', end_time - start_time)

# 行列乗算(2): C2 = A * B
start_time = time.time()
cmatrix_c2 = cmatrix_a.dot(cmatrix_b)
end_time = time.time()
print('CC2 計算時間(秒): ', end_time - start_time)

# 検算: ||C1 - C2|| == 0?
print('||CC1 - CC2|| = ', np.linalg.norm(cmatrix_c1 - cmatrix_c2))
