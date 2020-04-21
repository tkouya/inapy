# logistic_function.py : ロジスティック写像

x = [0.7501] # 初期値を配列の先頭値に格納

# x[i+1]に値を追加
for i in range(0, 100):
	x.append(4 * x[i] * (1 - x[i]))

# x[0], x[10], ..., x[100]を表示
for i in range(0, 101):
	if i % 10 == 0:
		print(i,',', x[i]) 
