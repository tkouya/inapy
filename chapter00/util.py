# util.py: utilモジュール

# odd_even_multi3関数
def odd_even(x): # このxは引数，関数内でのみ有効
    if x % 2 == 0:
        # 4の倍数はここでチェックする必要がある
        if x % 4 == 0:
            print(x, ' is multiple(s) of 4.')
        else:
            print(x, ' is even.')
    elif x % 3 == 0:
        print(x, ' is multiple(s) of 3.')
    else:
        print(x, ' is odd but not multiple(s) of 3.')


# tkRationalクラス
# a = num, den -> num / den
class tkRational: 
    # 初期化
    def __init__(self, num, den):
        self.num, self.den = int(num), int(den) # 整数のみ扱う
        # 分母は常に正
        if self.den < 0:
            self.num, self.den = -self.num, abs(self.den)

    # 文字列化: "-5 / 3"と表示
    def __str__(self):
        return str(self.num) + ' / ' + str(self.den)
    
    # 最大公約数: ユークリッドの互除法
    def get_gcd(self, den0, den1):
        if den0 < den1:
            tmp = den0
            den0 = den1
            den1 = tmp
        
        a, b = den0, den1
        r = a % b
        while r > 0:
           a = b
           b = r
           r = a % b

        return b

    # 通分: 同じ分母で表現した2分数を返す
    def get_common_den(self, rat0, rat1):
        common_den = rat0.den * rat1.den / self.get_gcd(rat0.den, rat1.den)
        new_x = tkRational(rat0.num * (common_den / rat0.den), common_den)
        new_y = tkRational(rat1.num * (common_den / rat1.den), common_den)
        return new_x, new_y

    # 約分: 分子と分母の最大公約数で割る
    def reduce(self):
        common_fac = self.get_gcd(abs(int(self.num)), int(self.den))
        if common_fac > 1:
            self.num /= common_fac
            self.den /= common_fac

        return tkRational(self.num, self.den)
        
    # 加算: x + y
    def __add__(self, y):
        a, b = self.get_common_den(self, y)
        return tkRational(a.num + b.num, a.den).reduce()

    # 減算: x - y
    def __sub__(self, y):
        a, b = self.get_common_den(self, y)
        return tkRational(a.num - b.num, a.den).reduce()

    # 乗算: x * y
    def __mul__(self, y):
        return tkRational(self.num * y.num, self.den * y.den).reduce()

    # 除算: x / y
    def __truediv__(self, y):
        return tkRational(self.num * y.den, self.den * y.num).reduce()

    # 出力用
    __repr__ = __str__

# -------------------------------------
# Copyright (c) 2026 Tomonori Kouya
# All rights reserved.
# -------------------------------------
