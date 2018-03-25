name = 'Swagger'

if name.startswith('Swa'):
  print('name start with Swa')
if name.endswith('er'):
  print('name end with er')
if name.find('wa') != -1:
  print('wa is in Swagger')

# join
delimiter = '_*_'
arr = ['name1', 'name2', 'name3']
print('str join arr: ', delimiter.join(arr))