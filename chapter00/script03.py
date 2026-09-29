# script03.py: 3番目のPythonスクリプト
x = [0, 1, 2, 3, 4, 5]

# for文
for i in range(6):
    print('x[', i, '] = ', x[i])

# while文
i = len(x) - 1
while i >= 0:
    print('x[', i, '] = ', x[i])
    i -= 1

# if文
for i in range(len(x)):
    if x[i] % 2 == 0:
        print('x[', i, '] = ', x[i], ' is even.')
    elif x[i] % 3 == 0: 
        print('x[', i, '] = ', x[i], ' is multiple(s) of 3.')
    else:
        print('x[', i, '] = ', x[i], ' is odd but not mutiple(s) of 3.')

# リスト内包表現
oddlist = [x[i] for i in range(len(x)) if x[i] % 2 != 0]
print('oddlist = ', oddlist)

# 上記と同じ
oddlist = []
for i in range(len(x)):
    if x[i] % 2 != 0:
        oddlist.append(x[i])
print('oddlist = ', oddlist)

# -------------------------------------
# Copyright (c) 2025 Tomonori Kouya
# All rights reserved.
# -------------------------------------
