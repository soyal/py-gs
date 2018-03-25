# 字典
ab = {
  'a1': '美国华盛顿',
  'a2': '北京中关村',
  'a3': '上海迪士尼'
}

print('dictionary length: ', len(ab))

print('dictionary content is: ', end= '')
for key,value in ab.items():
  print('key: {}, value: {}'.format(key, value))

if 'a1' in ab:
  print('the a1 is exist in ab')

if 1 != 2:
  print('111')

