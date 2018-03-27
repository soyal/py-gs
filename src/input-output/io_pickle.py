import pickle

shoplistfile = './shoplist.data'

shoplist = ['apple', 'banana', 'pear']

f = open(shoplistfile, 'wb')

pickle.dump(shoplist, f)
f.close()

# 重新打开
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)