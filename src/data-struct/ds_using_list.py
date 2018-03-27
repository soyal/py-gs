# 基础数据类型
# tuple dict str list set 
# 数字类型
# int float complex bool

shop = ['a', 'b', 'c', 'd']

print('shop list len: {}'.format(len(shop)))
# print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格
print('these items are: ', end=' ')

for item in shop:
  print(item, end='')

print('\nappend aa')
shop.append('aa')
print('the shop is now: ', shop)
print('sort shop')
shop.sort()
print('after sort', shop)
