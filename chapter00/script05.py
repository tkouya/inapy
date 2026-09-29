# script05.py: 5番目のPythonスクリプト
import util

# グローバル変数
x = 123

# util.は必要
util.odd_even(324)
util.odd_even(2345)
util.odd_even(3456789)
util.odd_even(x) # グローバル変数x

# util.は不要
from util import odd_even

odd_even(324)
odd_even(2345)
odd_even(3456789)
odd_even(x) # グローバル変数x

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
