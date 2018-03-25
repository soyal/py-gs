# 序列

shoplist = ['abandon', 'banana', 'candy', 'dance']
name = 'stringtest'

print('shoplist -1: ', shoplist[-1])

# 同Array.prototype.slice
print('shoplist 1 to 3:', shoplist[1:3])
print('shoplist 1 to end:', shoplist[1:])
print('shoplist 1 to -1:', shoplist[1:-1])
print('shoplist start to end', shoplist[:])

print('name 1 to end:', name[1:])

# 可以传递第三个参数 step
print('shoplist start to end step:2', shoplist[::2])
# step < 0代表逆序
print('shoplist start to end step:-1', shoplist[::-1])
print('shoplist start to end step:-1', shoplist[::-2])