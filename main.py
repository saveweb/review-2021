import os

flag = 0
markdown = """#2021年终总结

<--! 此处待完善 -->
"""

with open('metadata.md', 'r') as f:
  file = f.read()
lines = file.splitlines()
lines = set(lines)
lines.discard('')
lines = list(lines)
lines.sort()

with open('metadata.md', 'w') as f:
    for line in lines:
        f.write(line+'\n')

with open('README.md', 'w') as f:
  for line in lines:
    if flag == 0:
        f.write(markdown+'\n'+'- '+line+'\n')
        flag = 1
    else:
        f.write('- '+line+'\n')
