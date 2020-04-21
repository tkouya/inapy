# 丸めモード変更
# [Windows&Linux] https://rafaelbarreto.wordpress.com/2009/03/30/controlling-fpu-rounding-modes-with-python/
# [macOS] https://stackoverflow.com/questions/16000574/tie-breaking-of-round-with-numpy

# OS種別
# https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
import platform

# 丸めモード定義
global FE_TOZERO, FE_DOWNWARD, FE_UPWARD, FE_TONEAREST
# set_rmode(丸めモード), 丸めモード = get_rmode()
global set_rmode, get_rmode

# DLL呼び出し
# from ctypes import cdll
from ctypes import *

# OS名
os_name = platform.system()

# Windows
if os_name == 'Windows':
	msvcrt = cdll.msvcrt
	MW_RC = 0x00000300
	set_rmode = lambda mode: msvcrt._controlfp_s(0, mode, MW_RC)
#	get_rmode = lambda     : msvcrt._controlfp_s(pointer(current_mode), 0, 0)
	FE_TOZERO = 0x00000300
	FE_DOWNWARD = 0x00000100
	FE_UPWARD = 0x00000200
	FE_TONEAREST = 0x00000000
	def get_rmode():
		current_rmode = c_uint()
		msvcrt._controlfp_s(byref(current_rmode), 0, 0)
		
		return current_rmode.value & MW_RC
# Linux
elif os_name == 'Linux':
	from ctypes.util import find_library
	libm = cdll.LoadLibrary(find_library('m'))
	set_rmode, get_rmode = libm.fesetround, libm.fegetround
	# x86
	FE_TOZERO = 0xc00
	FE_DOWNWARD = 0x400
	FE_UPWARD = 0x800
	FE_TONEAREST = 0
# macOS
elif os_name == "Darwin":
	from ctypes.util import find_library
	libc = cdll.LoadLibrary(find_library('c'))
	set_rmode, get_rmode = libc.fesetround, libc.fegetround
	# x86
	FE_TOZERO = 0xc00
	FE_DOWNWARD = 0x400
	FE_UPWARD = 0x800
	FE_TONEAREST = 0

# 丸めモード確認
def print_rmode():
	rmode = get_rmode()

	if rmode == FE_TOZERO: print('切り捨て')
	elif rmode == FE_DOWNWARD: print('-Infへの丸め')
	elif rmode == FE_UPWARD: print('+Infへの丸め')
	elif rmode == FE_TONEAREST: print('最近偶数値丸め')
	else: print('不明 ', rmode)

	return rmode
