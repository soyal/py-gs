# Set
test = set(['test1', 'test2', 'test3', 'test1'])
# ignore repeat element
print('test is: ', test)

print('is test1 in test:', 'test1' in test)

testp = test.copy()
testp.add('other')
print('testp.issuperset(test)', testp.issuperset(test))

test.remove('test1')
# 求交集
print('the intersection is: ', testp.intersection(test))