
poem = '''
const a = 1
console.log(a)
'''
# 写文件
f = open('./poem.js', 'w')

f.write(poem)

f.close()

# 读文件
f = open('./poem.js')

while True:
  line = f.readline()
  if(len(line) == 0):
    break
  print(line, end='')

f.close()