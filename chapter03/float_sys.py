# float_sys.py : 倍精度浮動小数点情報
import sys

print(sys.float_info)

print('sys.float_info.max     = ', float.hex(sys.float_info.max))
print('                       = ', sys.float_info.max)
print('sys.float_info.min     = ', float.hex(sys.float_info.min))
print('                       = ', sys.float_info.min)
print('true_min               = ', float.hex(sys.float_info.min / 2**52))
print('                       = ', sys.float_info.min / 2**52)
print('sys.float_info.epsilon = ', float.hex(sys.float_info.epsilon))
print('                       = ', sys.float_info.epsilon)

# -------------------------------------
# Copyright (c) 2021 Tomonori Kouya
# All rights reserved.
# -------------------------------------
