# script04.py: 4番目のPythonスクリプト

# グローバル変数
x = 123

# odd_even_multi3関数
def odd_even(x): # このxは引数，関数内でのみ有効
    if x % 2 == 0:
        print(x, ' is even.')
    elif x % 3 == 0:
        print(x, ' is multiple(s) of 3.')
    else:
        print(x, ' is odd but not multiple(s) of 3.')

# メイン関数
odd_even(324)
odd_even(2345)
odd_even(3456789)
odd_even(x) # グローバル変数x

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
