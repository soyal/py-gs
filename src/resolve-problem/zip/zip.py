import os
import sys

curdir = sys.path[0]

source = os.path.join(curdir, 'source')

target = os.path.join(curdir, 'target')

print('zip command start...')
command = 'zip -r {0} {1}'.format(target, source)
print('command: ', command)
if os.system(command) == 0:
  print('zip success')
else:
  print('zip fail')
