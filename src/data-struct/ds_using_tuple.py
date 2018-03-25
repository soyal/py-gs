zoo = ('dog', 'cat', 'elephant')

new_zoo = ('monkey', 'camel', zoo)

print('zoo length: ',len(zoo))
print('the last animal about old zoo is', new_zoo[2][2])

# len == 1的元组
tuple_len1 = ('a',)
print(type(tuple_len1))
print('len: ', len(tuple_len1)) # len, 1