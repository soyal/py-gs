import sys
import os

print('the argv of sys is:')
for i in sys.argv:
  print(i)

print('\nthe sys module path is: ', sys.path, '\n')

print('\n cwd is: ', os.getcwd())