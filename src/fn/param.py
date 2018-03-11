# a捕获第一个参数，*b捕获位置参数,**c捕获关键字参数
def fn_test(a, *b, **c):
  print('a: {0}'.format(a))
  for pp in b:
    print('params b: {0}'.format(pp))
  
  for cc in c:
    print('param c: {0}'.format(cc))

fn_test(1,2,3,4,aa='fs', bc='nihao')
# a: 1
# params b: 2
# params b: 3
# params b: 4
# param c: aa
# param c: bc
  