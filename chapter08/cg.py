# cg.py : Conjugate-Gradient法
import numpy as np
import scipy as spy
import scipy.linalg as slinalg
# 時間計測
import time

# CG法
def cg(vec_x, mat_a, vec_b, rtol, atol, max_times):
    dim = vec_x.size
    r = vec_b - mat_a.dot(vec_x)
    p = r
    init_norm_r = np.linalg.norm(r)
    old_norm_r = init_norm_r    
    # メインループ
    for times in range(max_times):
        ap = mat_a.dot(p)
        alpha = r.dot(p) / p.dot(ap)    
        vec_x = vec_x + alpha * p
        r = r - alpha * ap
        new_norm_r = np.linalg.norm(r)
        beta = new_norm_r * new_norm_r / (old_norm_r * old_norm_r)  
        # 収束判定
        if(new_norm_r <= (rtol * init_norm_r + atol)):
        	break

        p = r + beta * p    
        old_norm_r = new_norm_r

    return times, vec_x

# 行列サイズ
str_dim = input('正方行列サイズ dim = ')
dim = int(str_dim) # 文字列→整数

# (1)
mat_a = np.zeros((dim, dim))
for i in range(dim):
    for j in range(dim):
        mat_a[i, j] = float(min(i + 1, j + 1)) / float(max(i + 1, j + 1))

mat_a = mat_a.transpose() * mat_a
print(mat_a)

# x = [1 2 ... dim]
vec_true_x = spy.arange(1, dim + 1)
#print(vec_true_x)

# b = A * x
vec_b = mat_a @ vec_true_x

# CG法実行
# vec_x := 0
vec_x = np.zeros(dim)
start_time1 = time.time()
iterative_times, vec_x = cg(vec_x, mat_a, vec_b, 1.0e-10, 0.0, dim * 10)
time1  = time.time() - start_time1

relerr = slinalg.norm(vec_x - vec_true_x) / slinalg.norm(vec_true_x)
print('CG: iteration, time = ', iterative_times, time1, ', relerr(vec_x) = ', relerr)
