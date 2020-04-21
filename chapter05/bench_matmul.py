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
print('||C1 - C2|| = ', np.linalg.norm(matrix_c1 - matrix_c2) / np.linalg.norm(matrix_c1))

# 終了
#quit()

# 自作行列乗算
def mymatmul(mat_a, mat_b):
    row_dim  , mid_dim = mat_a.shape
    mid_dim_b, col_dim = mat_b.shape
 #   print('row_dim, mid_dim, col_dim = ', row_dim, mid_dim, col_dim)
    if mid_dim != mid_dim_b:
        print('A\'s col_dim = ', mid_dim, ', B\'s row_dim = ', mid_dim_b, ' are mismatched!.')
        return np.ndarray([0])
  
    mat_c = np.zeros((row_dim, col_dim))
    for i in range(0, row_dim):
        for j in range(0, col_dim):
            for k in range(0, mid_dim):
                mat_c[i, j] += mat_a[i, k] * mat_b[k, j]
  
    return mat_c

# 自作行列乗算
start_time = time.time()
matrix_c3 = mymatmul(matrix_a, matrix_b)
end_time = time.time()
print('C3 計算時間(秒): ', end_time - start_time)

# 検算: ||C2 - C3|| == 0?
print('||C2 - C3|| = ', np.linalg.norm(matrix_c2 - matrix_c3) / np.linalg.norm(matrix_c2))
