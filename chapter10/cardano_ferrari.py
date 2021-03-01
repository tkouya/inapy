# cardano_ferrari.py: Cardano法とFerrari法
import numpy as np # NumPy

# 解の公式（2次方程式）
# coef[0] * x**2 + coef[1] * x + coef[2] = 0
def quadratic_eq(coef):
    sols = np.array([np.complex(0, 0), np.complex(0, 0)])
    d = coef[1] ** 2 - 4 * coef[0] * coef[2]
    sols[0] = (-coef[1] + np.sqrt(d)) / (2 * coef[0])
    sols[1] = (-coef[1] - np.sqrt(d)) / (2 * coef[0])

    return sols
 

# 解の公式（3次方程式: Cardano法）
# coef[0] * x**3 + coef[1] * x**2 + coef[2] * x + coef[3] = 0
def cardano(coef):
    sols = np.array([np.complex(0, 0), np.complex(0, 0), np.complex(0, 0)])
    omega3 = np.exp(2 * np.pi / 3 * 1j)

    in_p = -coef[1]**2 / (9 * coef[0]**2) + coef[2] / (3 * coef[0])
    in_q = 2 * coef[1]**3 / (27 * coef[0]**3) - coef[2] * coef[1] / (3 * coef[0]**2) + coef[3] / coef[0]

    in_u = ((-in_q + np.sqrt(in_q**2 + 4 * in_p**3)) / 2)**(1.0/3.0)
    in_v = ((-in_q - np.sqrt(in_q**2 + 4 * in_p**3)) / 2)**(1.0/3.0)

    if in_p == 0:
        u = 0
        v = 0
    elif in_u != 0:
        u = in_u
        v = -in_p / u
    elif in_v != 0:
        v = in_v
        u = -in_p / v

    sols[0] = u + v - coef[1] / (3 * coef[0])
    sols[1] = omega3 * u + omega3**2 * v - coef[1] / (3 * coef[0])
    sols[2] = omega3**2 * u + omega3 * v - coef[1] / (3 * coef[0])

    return sols


# 解の公式（4次方程式: Ferrari法）
# coef[0] * x**4 + coef[1] * x**3 + coef[2] * x**2 + coef[3] * x + coef[4] = 0 
def ferrari(coef):
    sols = np.array([np.complex(0, 0), np.complex(0, 0), np.complex(0, 0), np.complex(0, 0)])
    in_p = -3 * coef[1]**2 / (8 * coef[0]**2) + coef[2] / coef[0]
    in_q = coef[1]**3 / (8 * coef[0]**3) - coef[2] * coef[1] / (2 * coef[0]**2) + coef[3] / coef[0]
    in_r = -3 * coef[1]**4 / (256 * coef[0]**4) + coef[2] * coef[1]**2 / (16 * coef[0]**3) - coef[3] * coef[1] / (4 * coef[0]**2) + coef[4] / coef[0]    
    # q == 0
    if in_q == 0:
        sols[0] =  np.sqrt((-in_p - np.sqrt(in_p**2 - 4 * in_r)) / 2)
        sols[1] = -np.sqrt((-in_p - np.sqrt(in_p**2 - 4 * in_r)) / 2)
        sols[2] =  np.sqrt((-in_p + np.sqrt(in_p**2 - 4 * in_r)) / 2)
        sols[3] = -np.sqrt((-in_p + np.sqrt(in_p**2 - 4 * in_r)) / 2)
    else:
        # Cardano法を適用
        in_coef3 = [1, -in_p, -4 * in_r, 4 * in_p * in_r - in_q**2]
        # 解の公式（3次方程式: Cardano法）
        in_zs = cardano(in_coef3)
        in_z = in_zs[0] # どれか一つでよい    
        # 解の公式（2次方程式)
        in_coef21 = [1, -np.sqrt(in_z - in_p), in_z / 2 + np.sqrt(in_z - in_p) * in_q / (2 * (in_z - in_p))]
        in_sols21 = quadratic_eq(in_coef21)
        in_coef22 = [1, np.sqrt(in_z - in_p), in_z / 2 - np.sqrt(in_z - in_p) * in_q / (2 * (in_z - in_p))]
        in_sols22 = quadratic_eq(in_coef22)
    
        sols[0] = in_sols21[0]
        sols[1] = in_sols21[1]
        sols[2] = in_sols22[0]
        sols[3] = in_sols22[1]

    sols[0] = sols[0] - coef[1] / (4 * coef[0])
    sols[1] = sols[1] - coef[1] / (4 * coef[0])
    sols[2] = sols[2] - coef[1] / (4 * coef[0])
    sols[3] = sols[3] - coef[1] / (4 * coef[0])

    return sols


# 多項式の係数(2次)
# (1 + i) * x**2 + i * x + 3 = 0
#p = np.poly1d([1 + 1j, 1j, 3])
#p = np.poly1d([1 + 0j, 1 + 0j, 1 + 0j, 1 + 0j])
p = np.poly1d([1 + 0j, 1 + 0j, 1 + 0j, 1 + 0j, 1 + 0j])

# 係数の出力
print('p = \n', p)

# 解の出力
#sols = quadratic_eq(p.coef)
#sols = cardano(p.coef)
sols = ferrari(p.coef)
print(sols)
print(p.roots)
 
# 検算: ほぼゼロになればよい
print('p(sols)  = ', np.polyval(p, sols))
print('p(roots) = ', np.polyval(p, p.roots))


# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
