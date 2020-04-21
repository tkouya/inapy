# 丸めモード変更
import rmode
import math

# R.T.Kneusel, "Numbers and Computers", Springer, 2015.
# Interval -> [left, right]
class Interval:

	# 開始前のデフォルト丸めモード
	#default_rmode = rmode.FE_TONEAREST
	default_rmode = rmode.get_rmode()

	# コンストラクタ
	def __init__(self, left, right = None):
		if right == None: self.left = left; self.right = left
		else: self.left = left; self.right = right

	# + : 加算
	def __add__(self, y):
		rmode.set_rmode(rmode.FE_DOWNWARD)
		left = self.left + y.left
		rmode.set_rmode(rmode.FE_UPWARD)
		right = self.right + y.right
		rmode.set_rmode(Interval.default_rmode)

		return Interval(left, right)

	# - : 減算
	def __sub__(self, y):
		rmode.set_rmode(rmode.FE_DOWNWARD)
		left = self.left - y.right
		rmode.set_rmode(rmode.FE_UPWARD)
		right = self.right - y.left
		rmode.set_rmode(Interval.default_rmode)

		return Interval(left, right)

	# - :マイナス
	def __neg__(self):
		left = -self.right
		right = -self.left

		return Interval(left, right)

	# * : 乗算
	def __mul__(self, y):
		if not isinstance(y, Interval): y = Interval(float(y))
		rmode.set_rmode(rmode.FE_DOWNWARD)
		left = min([self.left * y.left, self.right * y.left, self.left * y.right, self.right * y.right])
		rmode.set_rmode(rmode.FE_UPWARD)
		right = max([self.left * y.left, self.right * y.left, self.left * y.right, self.right * y.right])
		rmode.set_rmode(Interval.default_rmode)

		return Interval(left, right)

	__rmul__ = __mul__


	# recip(x) = 1/x: 逆数
	def recip(self):
		if (self.left < 0.0) and (self.right > 0.0):
			return Interval(-math.inf, math.inf)

		rmode.set_rmode(rmode.FE_DOWNWARD)
		left = 1.0 / self.right
		rmode.set_rmode(rmode.FE_UPWARD)
		right = 1.0 / self.left
		rmode.set_rmode(Interval.default_rmode)

		return Interval(left, right)

	# / : 除算
	def __truediv__(self, y):
		return self.__mul__(y.recip())

	# 絶対値
	def abs(self):
		return max([math.abs(self.left), math.abs(self.right)])

	# 平方根
	def sqrt(self):
		if (self.left < 0) or (self.right < 0):
			return Interval(-math.nan, -math.nan)

		return Interval(math.sqrt(self.left), math.sqrt(self.right))

	# ** : べき乗
	def __pow__(self, n):
		if (n % 2) == 1:
			rmode.set_rmode(rmode.FE_DOWNWARD)
			left = self.left ** n
			rmode.set_rmode(rmode.FE_UPWARD)
			right = self.right ** n
		elif self.left >= 0:
			rmode.set_rmode(rmode.FE_DOWNWARD)
			left = self.left ** n
			rmode.set_rmode(rmode.FE_UPWARD)
			right = self.right ** n
		elif self.right < 0:
			rmode.set_rmode(rmode.FE_DOWNWARD)
			left = self.right ** n
			rmode.set_rmode(rmode.FE_UPWARD)
			right = self.left ** n
		else:
			left = 0.0
			rmode.set_rmode(rmode.FE_UPWARD)
			right = self.left ** n
			temp = self.right ** n
			if temp > right: right = temp

		rmode.set_rmode(Interval.default_rmode)
		return Interval(left, right)

	# 出力用
	def __str__(self):
		return "[ %g, %g ]" % (self.left, self.right)

	__repr__ = __str__

