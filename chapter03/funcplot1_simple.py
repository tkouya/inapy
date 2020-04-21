# 関数グラフ
# https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
# ライブラリ名のエイリアス
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np # 数値データ，数学関数

# 関数データを作成
# y = f(x)
# x = numpy.arange(0.0, 7.0, 0.1) # x in [0 : 0.1 : 2]
# y = numpy.sin(x)
#x = np.arange(0.0, 7.0, 0.1) # x in [0 : 0.1 : 2]
x = np.linspace(0.0, 7.0)
# y = np.sin(x)
# y = np.cos(x)
# y = np.tan(x)
y = np.exp(x)
# y = np.log(x)

# 確認
#print('x = ', x)
#print('y = ', y)

# グラフ初期化
# figure, axis = matplotlib.pyplot.subplots()
figure, axis = plt.subplots()

# 値をセット
axis.plot(x, y)

# x軸，y軸，グラフタイトルをセット
axis.set(xlabel = 'x', ylabel = 'y', title = 'y = sin(x)')

# グリッドを描画
axis.grid()

# グラフ保存ファイル名
figure.savefig('sin.png')

# グラフを画面に描画
# matplotlib.pyplot.show()
plt.show()





