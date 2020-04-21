# print_format.py: 型指定出力
a = 3.1415926535
print(f'a = {a:25.17e}')
print(f'a = {a:+15.3f}')
print(f'a = {a:25.17g}')

print('a = {:25.17e}'.format(a))
