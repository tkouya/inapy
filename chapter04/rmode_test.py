# 丸めモード変更
import rmode
import sys

# テスト
default_rmode = rmode.print_rmode()
print('sys.float_info.rounds = ', sys.float_info.rounds)

# 切り捨て
rmode.set_rmode(rmode.FE_TOZERO)
rmode.print_rmode()
print('sys.float_info.rounds = ', sys.float_info.rounds)

# +infへの丸め
rmode.set_rmode(rmode.FE_UPWARD)
rmode.print_rmode()
print('sys.float_info.rounds = ', sys.float_info.rounds)

# -infへの丸め
rmode.set_rmode(rmode.FE_DOWNWARD)
rmode.print_rmode()
print('sys.float_info.rounds = ', sys.float_info.rounds)

# 元に戻す
rmode.set_rmode(default_rmode)
rmode.print_rmode()
print('sys.float_info.rounds = ', sys.float_info.rounds)
